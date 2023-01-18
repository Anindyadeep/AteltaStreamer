## **AteltaAI Streamer SDK** 

Official repository for **AteltaAI** Streamer SDK. This repository helps to establish the two video streams 
across different types of video sources. 

This repository will be shifted to **[CookieClutter-DataSc](https://github.com/drivendata/cookiecutter-data-science)** soon.

### **How to run the Project**

First install the required dependencies on your virtual environment

```bash 

pip install -r requirements.txt
```

- Then for geting a video get processed, first download a video (For now the automatic download is not implemented). So download a video / or any existing video that contains any action. Lets assume the name of the video is `sample_video.mp4`. 


- Save the video in `RawData/` folder.

- In order to preprocess the video run the following command:

```bash
PYTHONPATH=. python3 python3 src/stream.py -s1 RawData/sample_video.mp4
```
- The above steps does all the required preprocessing. Which includes: 
    - Generating the keypoints 
    - Drawing the keypoints on the video 
    - Saving the keypoints on a file 
    And it creates a file structure something like this:
    ```
    .DATA/
    └── sample_video
        ├── sample_video_key_frames
        ├── sample_video.mp4
        └── sample_video_preprocessed.mp4
    ```

- In order to run the two video streams using that preprocessed video on the webcam, go to `two_video_stream.py` And run the following command:
    ```bash 
    PYTHONPATH=. python3 two_video_stream.py -s1 <The name of the video>
    ```

    Here it will be:
    ```
    PYTHONPATH=. python3 two_video_stream.py -s1 sample_video
    ```