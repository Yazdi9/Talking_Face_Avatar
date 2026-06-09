"""Unified text-to-speech provider interface for ElevenLabs and 60db.

Both providers expose an identical surface so callers can switch freely::

    from src.utils.tts_providers import get_provider

    provider = get_provider("60db")          # or "elevenlabs"
    path = provider.synthesize("Hello world", output_path="output.mp3")

`synthesize()` always returns the path to an audio file written to disk,
ready to feed straight into SadTalker (which converts MP3 -> WAV internally,
see `src/gradio_demo.py::mp3_to_wav`).

Design notes -- the two upstream APIs differ; this module normalizes them:

  * Auth         ElevenLabs uses an `xi-api-key` header; 60db uses
                 `Authorization: Bearer <key>`.
  * Response     ElevenLabs returns raw MP3 bytes; 60db returns JSON with a
                 base64 `audio_base64` field which we decode to bytes.
  * Voice id     ElevenLabs puts it in the URL path; 60db puts it in the body.
  * stability /  Callers always pass these on a 0.0-1.0 scale (ElevenLabs's
    similarity   native range). The 60db provider rescales to its 0-100 range.

API keys are read from environment variables (never hard-coded):

  * ELEVENLABS_API_KEY
  * SIXTYDB_API_KEY

A local `.env` file is loaded automatically if `python-dotenv` is installed.
"""

import os
import sys
import json
import base64

import requests

# Best-effort .env loading; optional dependency.
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover - dotenv is optional
    pass


def _to_100(value):
    """Convert a 0.0-1.0 fraction (ElevenLabs scale) to 0-100 (60db scale).

    Values already greater than 1 are assumed to be on the 0-100 scale and
    passed through unchanged, so callers can use either convention.
    """
    if value is None:
        return None
    return round(value * 100) if value <= 1 else round(value)


class TTSProvider:
    """Common interface. Subclasses implement :meth:`synthesize`."""

    name = "base"
    env_key = None
    #: voice id used when the caller does not specify one (None = API default)
    default_voice = None

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get(self.env_key or "")
        if not self.api_key:
            raise ValueError(
                f"Missing API key for provider '{self.name}'. "
                f"Set the {self.env_key} environment variable "
                f"(or a .env file) or pass api_key=..."
            )

    def synthesize(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        **kwargs,
    ):
        """Synthesize `text` to an audio file and return its path.

        Parameters are normalized across providers:

        * ``stability`` / ``similarity`` -- floats in ``[0.0, 1.0]``.
        * ``speed`` -- playback rate multiplier (honored by 60db only;
          ElevenLabs's monolingual v1 endpoint has no speed control).
        * ``output_format`` -- one of ``mp3``/``wav``/``ogg``/``flac`` for
          60db; ElevenLabs always returns ``mp3`` for this endpoint.
        """
        raise NotImplementedError

    def synthesize_stream(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        **kwargs,
    ):
        """Stream synthesis, writing audio to `output_path` as it arrives.

        Same return contract as :meth:`synthesize` -- returns the path to the
        completed audio file -- so it drops straight into the SadTalker
        pipeline. The difference is that audio is written incrementally as the
        provider streams chunks, instead of buffering the whole response.
        """
        raise NotImplementedError

    def get_voices(self):
        """Return the list of available voices for this provider.

        Each item is a dict containing at least ``voice_id`` and ``name``
        (both providers expose those keys), plus provider-specific metadata.
        """
        raise NotImplementedError

    @staticmethod
    def _write(path, audio_bytes):
        with open(path, "wb") as f:
            f.write(audio_bytes)
        return path


class ElevenLabsProvider(TTSProvider):
    name = "elevenlabs"
    env_key = "ELEVENLABS_API_KEY"
    base_url = "https://api.elevenlabs.io/v1"
    default_voice = "EXAVITQu4vr4xnSDxMaL"  # Bella
    default_model = "eleven_monolingual_v1"

    def synthesize(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        model_id=None,
        **kwargs,
    ):
        voice_id = voice_id or self.default_voice
        output_path = output_path or "output.mp3"
        url = f"{self.base_url}/text-to-speech/{voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key,
        }
        data = {
            "text": text,
            "model_id": model_id or self.default_model,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity,
            },
        }
        resp = requests.post(url, json=data, headers=headers, timeout=120)
        resp.raise_for_status()
        return self._write(output_path, resp.content)

    def synthesize_stream(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        model_id=None,
        **kwargs,
    ):
        voice_id = voice_id or self.default_voice
        output_path = output_path or "output.mp3"
        url = f"{self.base_url}/text-to-speech/{voice_id}/stream"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key,
        }
        data = {
            "text": text,
            "model_id": model_id or self.default_model,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity,
            },
        }
        resp = requests.post(
            url, json=data, headers=headers, stream=True, timeout=120
        )
        resp.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return output_path

    def get_voices(self):
        url = f"{self.base_url}/voices"
        headers = {"Accept": "application/json", "xi-api-key": self.api_key}
        resp = requests.get(url, headers=headers, timeout=60)
        resp.raise_for_status()
        return resp.json().get("voices", [])


class SixtyDBProvider(TTSProvider):
    name = "60db"
    env_key = "SIXTYDB_API_KEY"
    base_url = "https://api.60db.ai"
    default_voice = None  # 60db falls back to a system default voice
    max_chars = 5000

    def synthesize(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        enhance=True,
        **kwargs,
    ):
        if len(text) > self.max_chars:
            raise ValueError(
                f"60db TTS accepts at most {self.max_chars} characters per "
                f"request (got {len(text)})."
            )
        voice_id = voice_id or self.default_voice
        output_path = output_path or f"output.{output_format}"
        url = f"{self.base_url}/tts-synthesize"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "text": text,
            "enhance": enhance,
            "speed": speed,
            "stability": _to_100(stability),
            "similarity": _to_100(similarity),
            "output_format": output_format,
        }
        if voice_id:
            data["voice_id"] = voice_id

        resp = requests.post(url, json=data, headers=headers, timeout=120)
        resp.raise_for_status()
        payload = resp.json()
        if not payload.get("success", True):
            raise RuntimeError(
                f"60db TTS failed: {payload.get('message', 'unknown error')}"
            )
        audio_b64 = payload.get("audio_base64")
        if not audio_b64:
            raise RuntimeError("60db TTS response did not contain audio_base64")
        return self._write(output_path, base64.b64decode(audio_b64))

    def synthesize_stream(
        self,
        text,
        output_path=None,
        voice_id=None,
        stability=0.5,
        similarity=0.75,
        speed=1.0,
        output_format="mp3",
        enhance=True,
        **kwargs,
    ):
        if len(text) > self.max_chars:
            raise ValueError(
                f"60db TTS accepts at most {self.max_chars} characters per "
                f"request (got {len(text)})."
            )
        voice_id = voice_id or self.default_voice
        output_path = output_path or f"output.{output_format}"
        url = f"{self.base_url}/tts-stream"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "text": text,
            "enhance": enhance,
            "speed": speed,
            "stability": _to_100(stability),
            "similarity": _to_100(similarity),
        }
        if voice_id:
            data["voice_id"] = voice_id

        resp = requests.post(
            url, json=data, headers=headers, stream=True, timeout=120
        )
        resp.raise_for_status()
        # Response is newline-delimited JSON: one object per line. "chunk"
        # objects carry base64 audio, "complete" ends the stream, "error"
        # signals failure.
        with open(output_path, "wb") as f:
            for line in resp.iter_lines(decode_unicode=True):
                if not line:
                    continue
                msg = json.loads(line)
                msg_type = msg.get("type")
                if msg_type == "chunk":
                    audio_b64 = (msg.get("result") or {}).get("audioContent")
                    if audio_b64:
                        f.write(base64.b64decode(audio_b64))
                elif msg_type == "error":
                    raise RuntimeError(
                        f"60db TTS stream error: "
                        f"{msg.get('message', 'unknown error')}"
                    )
                elif msg_type == "complete":
                    break
        return output_path

    def get_voices(self):
        url = f"{self.base_url}/myvoices"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        resp = requests.get(url, headers=headers, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
        if not payload.get("success", True):
            raise RuntimeError(
                f"60db get_voices failed: "
                f"{payload.get('message', 'unknown error')}"
            )
        return payload.get("data", [])


_PROVIDERS = {
    "elevenlabs": ElevenLabsProvider,
    "60db": SixtyDBProvider,
    "sixtydb": SixtyDBProvider,
}


def get_provider(name, api_key=None):
    """Return an initialized TTS provider by name.

    Accepted names: ``"elevenlabs"``, ``"60db"`` (alias ``"sixtydb"``).
    """
    key = (name or "").lower().strip()
    if key not in _PROVIDERS:
        raise ValueError(
            f"Unknown TTS provider '{name}'. "
            f"Available: {sorted(set(_PROVIDERS))}"
        )
    return _PROVIDERS[key](api_key=api_key)


def synthesize(text, provider="60db", **kwargs):
    """Convenience one-liner: pick a provider and synthesize in one call."""
    return get_provider(provider).synthesize(text, **kwargs)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate speech audio with ElevenLabs or 60db."
    )
    parser.add_argument("text", nargs="?", default=None,
                        help="Text to synthesize (omit with --list-voices).")
    parser.add_argument(
        "--provider",
        default="60db",
        choices=sorted(set(_PROVIDERS)),
        help="TTS provider (default: 60db).",
    )
    parser.add_argument("--voice", default=None, help="Voice id.")
    parser.add_argument("--out", default=None, help="Output audio file path.")
    parser.add_argument("--stability", type=float, default=0.5,
                        help="0.0-1.0 (default 0.5).")
    parser.add_argument("--similarity", type=float, default=0.75,
                        help="0.0-1.0 (default 0.75).")
    parser.add_argument("--speed", type=float, default=1.0,
                        help="Speed multiplier, 60db only (default 1.0).")
    parser.add_argument("--format", default="mp3",
                        help="Output format: mp3/wav/ogg/flac (60db).")
    parser.add_argument("--stream", action="store_true",
                        help="Use streaming synthesis.")
    parser.add_argument("--list-voices", action="store_true",
                        help="List available voices for the provider and exit.")
    args = parser.parse_args()

    provider = get_provider(args.provider)

    if args.list_voices:
        for voice in provider.get_voices():
            print(f"{voice.get('voice_id')}\t{voice.get('name')}")
        sys.exit(0)

    if not args.text:
        parser.error("the 'text' argument is required unless --list-voices is set")

    method = provider.synthesize_stream if args.stream else provider.synthesize
    out_path = method(
        args.text,
        voice_id=args.voice,
        output_path=args.out,
        stability=args.stability,
        similarity=args.similarity,
        speed=args.speed,
        output_format=args.format,
    )
    verb = "streamed" if args.stream else "wrote"
    print(f"[{args.provider}] {verb} {out_path}")
