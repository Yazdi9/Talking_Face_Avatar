<div align="center">



 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Winfredy/SadTalker/blob/main/quick_demo.ipynb) &nbsp; 


<b>Talking Face Avatar:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; single portrait image From Leonardo.ai API 🙎‍♂️ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; audio From ElevenLabs TTS API 🎤 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; talking head video 🎞.</b>

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
 
<img src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/b3f5baa3-93be-4e5b-b492-acebbdb4c9e9" width="300px";height:"400px">

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




## 🔥 Highlight


-🔥 Scroll To left and Right To See All Videos


| video 1 + enhancer(GFPGAN )                | video 2      |  video 3 |
|:--------------------: |:--------------------: | :----: |
| <video src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/7879fcc4-fe3c-473a-86d8-23c736dd4a65.mp4" type="video/mp4"> </video> | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/a7eb4df8-1789-412d-97da-8f6b361a72a2.mp4" type="video/mp4"> </video>  | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/b20102bd-852a-4091-87da-18dba720bc93.mp4" type="video/mp4"> </video>

| video 4                | video 5     |  video 6 |
|:--------------------: |:--------------------: | :----: |
| <video src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/91be247e-b1e4-4206-aa95-4eca938597b2.mp4" type="video/mp4"> </video> | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/18c7fc59-00f9-4118-b88b-545d3ea87342.mp4" type="video/mp4"> </video>  | <video  src="https://github.com/saba99/Talking_Face_Avatar/assets/33378412/f0bc6062-1a81-44f7-b6bc-747df6c06568.mp4" type="video/mp4"> </video>

- 🔥 Several new mode, eg, `still mode`, `reference mode`, `resize mode` are online for better and custom applications.


### Linux:

1. Installing [anaconda](https://www.anaconda.com/), python and git.

2. Creating the env and install the requirements.
  ```bash
  git clone https://github.com/Winfredy/SadTalker.git

  cd SadTalker 

  conda create -n sadtalker python=3.8

  conda activate sadtalker

  pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

  conda install ffmpeg

  pip install -r requirements.txt

  ### tts is optional for gradio demo. 
  ### pip install TTS

  ```  
### Windows ([windows](https://www.bilibili.com/video/BV1Dc411W7V6/)):

1. Install [Python 3.10.6](https://www.python.org/downloads/windows/), checking "Add Python to PATH".
2. Install [git](https://git-scm.com/download/win) manually (OR `scoop install git` via [scoop](https://scoop.sh/)).
3. Install `ffmpeg`, following [this instruction](https://www.wikihow.com/Install-FFmpeg-on-Windows) (OR using `scoop install ffmpeg` via [scoop](https://scoop.sh/)).
4. Download our SadTalker repository, for example by running `git clone https://github.com/Winfredy/SadTalker.git`.
5. Download the `checkpoint` and `gfpgan` [below↓](https://github.com/Winfredy/SadTalker#-2-download-trained-models).
5. Run `start.bat` from Windows Explorer as normal, non-administrator, user, a gradio WebUI demo will be started.


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



