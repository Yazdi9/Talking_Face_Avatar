<div align="center">

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/sabahesaraY)


 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Winfredy/SadTalker/blob/main/quick_demo.ipynb) &nbsp; 


<b>Talking Face Avatar:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; single portrait image From Leonardo.ai API 🙎‍♂️ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; audio From ElevenLabs / 60db TTS API 🎤 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; talking head video 🎞.</b>

<br>

</div>

## Leonardo.ai 

Go To [Leonardo.Ai](https://app.leonardo.ai/ai-generations) And Enter your Prompt And Negative Prompts To Generate Artistic Images

Here Some Recources :[Leonardo.ai Youtube Video](https://www.youtube.com/watch?v=36rSjS5hV4Y)
                     [Leonardo.ai Youtube Video Toutorial](https://www.youtube.com/watch?v=XW7CyTPd0aI&list=PL3qnMcmlvPBHvhxHL2wVHSzN870Y-wWVa)
                     
or you can use APIs [Leonardo.Ai API Guide](https://docs.leonardo.ai/docs) 

<table class="center">
<tr>
  <td style="text-align:center;"><b>Leonardo.ai Image Generation</b></td>
  <td style="text-align:center;"><b>Leonardo.ai Image Generation</b></td>
   <td style="text-align:center;"><b>Leonardo.ai Image Generation</b></td>
</tr>
  
<tr>
<td>
<img src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/12ffc93b-79f5-4cf0-a14d-f58cc050cc16" width="300px";height:"400px">

</td>
<td>
 <img src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/ef923464-1033-45ba-a067-2a21afbae8fa" width="300px";height:"400px">

</td>
<td>
 <img src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/cfb315c5-35f8-4a76-945d-eca0393825b0" width="300px";height:"400px">


</td>

</tr>
</table>


## ElevenLabs 

Go To [Eleven Labs](https://beta.elevenlabs.io/) And Enter your Text And Generate Beautiful Audios With Diffrent Pitchs and Speeckers. ElvenLabs also is Multilingual 

Here Some Recources :[ElevenLabs Youtube Video](https://www.youtube.com/watch?v=CYGwfHWiSyU)

or you can use APIs [ElevenLabs API Guide](https://api.elevenlabs.io/docs) 

[ElevenLabs Python Repo](https://github.com/lugia19/elevenlabslib)


<table class="center">
<tr>
  <td style="text-align:center;"><b>Eleven Labs TTS</b></td>
  <td style="text-align:center;"><b>Eleven Labs TTS</b></td>
   <td style="text-align:center;"><b>Eleven Labs TTS</b></td>
</tr>
  
<tr>
<td>


https://github.com/saba99/Talking_Face_Avatar/assets/33378412/bd68137d-2e67-41df-a1df-4162db170ff8


</td>
<td>

https://github.com/saba99/Talking_Face_Avatar/assets/33378412/f622369b-9e69-492d-975b-685671c663c1

</td>
<td>

https://github.com/saba99/Talking_Face_Avatar/assets/33378412/1f78eb67-cc76-4c9a-8664-a28f3f795bee

</td> 

 
</tr>


</table>




## 60db TTS

[60db](https://60db.ai/) is an alternative multilingual TTS provider (English plus Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Punjabi, Tamil and Telugu). It can be used in place of ElevenLabs to generate the driving audio for the talking head.

API guide: [60db TTS docs](https://docs.60db.ai/api-reference/tts/text-to-speech) &nbsp;|&nbsp; [Streaming](https://docs.60db.ai/api-reference/tts/text-to-speech-stream) &nbsp;|&nbsp; [Voices](https://docs.60db.ai/api-reference/voices/get-my-voices)

Key differences from ElevenLabs (all handled for you by the unified library below):

| | ElevenLabs | 60db |
| :--- | :--- | :--- |
| Auth header | `xi-api-key` | `Authorization: Bearer` |
| TTS endpoint | `POST /v1/text-to-speech/{voice_id}` | `POST /tts-synthesize` |
| Stream endpoint | `POST /v1/text-to-speech/{voice_id}/stream` | `POST /tts-stream` |
| List voices | `GET /v1/voices` | `GET /myvoices` |
| Response | raw MP3 bytes | JSON `audio_base64` (TTS) / NDJSON base64 chunks (stream) |
| `stability` / `similarity` | `0.0`–`1.0` | `0`–`100` |
| Voice id | alphanumeric (`ErXwobaYiN019PkySvjV`) | UUID (`fbb75ed2-...`) |

Both providers implement the same three methods in the library —
`synthesize()`, `synthesize_stream()` and `get_voices()` — so they stay fully
interchangeable.

## Unified TTS Library

`src/utils/tts_providers.py` exposes ElevenLabs and 60db behind one identical interface, so you can switch providers without changing your code. Every call returns the path to an audio file on disk, ready to feed into SadTalker (which converts MP3 → WAV internally).

**1. Configure API keys** (never hard-coded — read from the environment):

```bash
cp .env.example .env
# then edit .env and set:
#   ELEVENLABS_API_KEY=...
#   SIXTYDB_API_KEY=sk_live_...
```

`.env` is auto-loaded if [`python-dotenv`](https://pypi.org/project/python-dotenv/) is installed (`pip install python-dotenv`); otherwise export the variables in your shell.

**2. Use it from Python:**

```python
from src.utils.tts_providers import get_provider, synthesize

# 60db
path = get_provider("60db").synthesize(
    "Hello world", output_path="output.mp3", voice_id="fbb75ed2-..."
)

# ElevenLabs — identical call signature
path = get_provider("elevenlabs").synthesize(
    "Hello world", output_path="output.mp3", voice_id="EXAVITQu4vr4xnSDxMaL"
)

# one-liner convenience wrapper
synthesize("Hello world", provider="60db")
```

`stability` and `similarity` are always passed on a `0.0`–`1.0` scale; the 60db provider rescales them to its `0`–`100` range automatically.

**3. Streaming** — `synthesize_stream()` writes audio incrementally as it arrives and returns the same file path, so it drops into the pipeline exactly like `synthesize()`:

```python
path = get_provider("60db").synthesize_stream("Hello world", output_path="output.mp3")
path = get_provider("elevenlabs").synthesize_stream("Hello world", output_path="output.mp3")
```

**4. List available voices** — `get_voices()` returns a list of voice dicts (each has at least `voice_id` and `name`):

```python
for v in get_provider("60db").get_voices():
    print(v["voice_id"], v["name"])
```

**5. Or from the command line:**

```bash
# synthesize
python -m src.utils.tts_providers "Hello world" --provider 60db --voice <voice_id> --out output.mp3
python -m src.utils.tts_providers "Hello world" --provider elevenlabs --out output.mp3

# streaming
python -m src.utils.tts_providers "Hello world" --provider 60db --stream --out output.mp3

# list voices (no text needed)
python -m src.utils.tts_providers --provider 60db --list-voices
```

The resulting audio file can then be uploaded as the **Input audio** in the Gradio demo, or passed to `inference.py --driven_audio output.mp3`.

> ⚠️ **Security:** older scripts in `api/` contain hard-coded API keys. Treat those as compromised and rotate them; the unified library reads keys only from environment variables.

## 🔥 Highlight


-🔥 Scroll To left and Right To See All Videos


| video 1 + enhancer(GFPGAN )                | video 2      |  video 3 |
|:--------------------: |:--------------------: | :----: |
| <video src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/7879fcc4-fe3c-473a-86d8-23c736dd4a65.mp4" type="video/mp4"> </video> | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/a7eb4df8-1789-412d-97da-8f6b361a72a2.mp4" type="video/mp4"> </video>  | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/b20102bd-852a-4091-87da-18dba720bc93.mp4" type="video/mp4"> </video>

| video 4                | video 5     |  video 6 |
|:--------------------: |:--------------------: | :----: |
| <video src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/91be247e-b1e4-4206-aa95-4eca938597b2.mp4" type="video/mp4"> </video> | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/18c7fc59-00f9-4118-b88b-545d3ea87342.mp4" type="video/mp4"> </video>  | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/f0bc6062-1a81-44f7-b6bc-747df6c06568.mp4" type="video/mp4"> </video>

- 🔥 Several new mode, eg, `still mode`, `reference mode`, `resize mode` are online for better and custom applications.

## Our Diagram Approach


![you_doodle_pro_2023-05-19t16_25_09z](https://github.com/saba99/Talking_Face_Avatar/assets/33378412/a516b0fb-7ab5-4fd3-b78c-79808e8eec6e)



### Linux:

1. Installing [anaconda](https://www.anaconda.com/), python and git.

2. Creating the env and install the requirements.
  ```bash
  git clone https://github.com/saba99/Talking_Face_Avatar.git

  cd SadTalker 

  conda create -n sadtalker python=3.8

  conda activate sadtalker

  pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

  conda install ffmpeg

  pip install -r requirements.txt

  ### tts is optional for gradio demo. 
  ### pip install TTS

  ```  
### UI + API:
  look at index.html 

![Screenshot (4899)](https://github.com/saba99/Talking_Face_Avatar/assets/33378412/f922a6e8-38da-4b2a-b339-7a689dc33bc9) 


## 📥 2. Download Trained Models.

You can run the following script to put all the models in the right place.




```bash
bash scripts/download_models.sh
```

<details><summary>Model Details</summary>

The final folder will be shown as:

<img width="331" alt="image" src="https://user-images.githubusercontent.com/4397546/232511411-4ca75cbf-a434-48c5-9ae0-9009e8316484.png">


Model explains:

| Model | Description
| :--- | :----------
|checkpoints/auido2exp_00300-model.pth | Pre-trained ExpNet in Sadtalker.
|checkpoints/auido2pose_00140-model.pth | Pre-trained PoseVAE in Sadtalker.
|checkpoints/mapping_00229-model.pth.tar | Pre-trained MappingNet in Sadtalker.
|checkpoints/mapping_00109-model.pth.tar | Pre-trained MappingNet in Sadtalker.
|checkpoints/facevid2vid_00189-model.pth.tar | Pre-trained face-vid2vid model from [the reappearance of face-vid2vid](https://github.com/zhanglonghao1992/One-Shot_Free-View_Neural_Talking_Head_Synthesis).
|checkpoints/epoch_20.pth | Pre-trained 3DMM extractor in [Deep3DFaceReconstruction](https://github.com/microsoft/Deep3DFaceReconstruction).
|checkpoints/wav2lip.pth | Highly accurate lip-sync model in [Wav2lip](https://github.com/Rudrabha/Wav2Lip).
|checkpoints/shape_predictor_68_face_landmarks.dat | Face landmark model used in [dilb](http://dlib.net/). 
|checkpoints/BFM | 3DMM library file.  
|checkpoints/hub | Face detection models used in [face alignment](https://github.com/1adrianb/face-alignment).
|gfpgan/weights | Face detection and enhanced models used in `facexlib` and `gfpgan`.


</details>

## 🔮 3. Quick Start ([Best Practice](docs/best_practice.md)).

### WebUI Demos:

 [SDWebUI-Colab](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/video/stable/stable_diffusion_1_5_video_webui_colab.ipynb) | [Colab](https://colab.research.google.com/github/Winfredy/SadTalker/blob/main/quick_demo.ipynb)

```bash
## you need manually install TTS(https://github.com/coqui-ai/TTS) via `pip install tts` in advanced.
python app.py
```

### Manually usages:

##### Animating a portrait image from default config:
```bash
python inference.py --driven_audio <audio.wav> \
                    --source_image <video.mp4 or picture.png> \
                    --enhancer gfpgan 
```
The results will be saved in `results/$SOME_TIMESTAMP/*.mp4`.

##### Full body/image Generation:

Using `--still` to generate a natural full body video. You can add `enhancer` to improve the quality of the generated video. 

```bash
python inference.py --driven_audio <audio.wav> \
                    --source_image <video.mp4 or picture.png> \
                    --result_dir <a file to store results> \
                    --still \
                    --preprocess full \
                    --enhancer gfpgan 
```


[![Star History Chart](https://api.star-history.com/svg?repos=yazdi9/Talking_Face_Avatar&type=Date)](https://star-history.com/#yazdi9/Talking_Face_Avatar&Date)
