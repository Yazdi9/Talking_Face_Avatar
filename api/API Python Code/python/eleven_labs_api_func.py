
import requests 
import json 

CHUNK_SIZE = 1024

#get_voices

def get_voices():

    url = "https://api.elevenlabs.io/v1/voices"

    payload = {}
    headers = {
    'accept': 'application/json',
    'xi-api-key': '128c3bf75d5ccb4d0b18af829bc9d763'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

#text to speech 
    
def  text_to_speech():
    
    
    url = "https://api.elevenlabs.io/v1/text-to-speech/ErXwobaYiN019PkySvjV"
    
    headers = {
    'Accept': 'audio/mpeg',
    'Content-Type': 'application/json',
    'xi-api-key': '16bc562d24b6090fe5035c9458707fe9'
    
    }

    data = {
        "text": "Hi! My name is Bella, nice to meet you!",
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
   

    #response = requests.request("POST", url, headers=headers, data=data)
    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    return response.text




get_voice=get_voices()
print(get_voice)

tts=text_to_speech()
print(tts)






    