## Introduction
This video project has been created through __coding__ for a university design class. The project features music(__당신의 밤 (feat. 오혁)/황광희 X 개코__) dedicated to Yoon Dong-ju, a renowned Korean poet who fought for the independence of his country, Korea.


[![Watch the video](https://img.youtube.com/vi/qnzjKgrjXq8/0.jpg)](https://youtu.be/qnzjKgrjXq8)


## About Video
This project video consists of three parts.

The first part of the video shows texts that symbolize world peace and innocence, but these texts suddenly disappear when confronted with the world's cruelty. Simultaneously, a white frame slowly expands, representing the prison where poet Yoon Dong-ju was incarcerated during the Japanese colonial period for his defiant poetry. Like a lantern facing a strong wind, the yellow flame appears precarious.

<img width="60%" src="https://github.com/DIYongSeok/interactive-video-using-hand-tracking/assets/146920174/039e5fae-394c-42e2-b2be-ac53f152a37f"/>

<br/><br/>
The second part of the video shows faint fireflies flying across the raining screen and a red dot representing the position of your hand. When the red dot comes close enough to the fireflies through the movement of your hand, it reveals words from Yoon Dong-ju's poem "Counting the Stars at Night," expressing his longing for his hometown, family, and childhood memories.

<img width="60%" src="https://github.com/DIYongSeok/interactive-video-using-hand-tracking/assets/146920174/958de0d0-b64c-4d8f-9e37-a14e15e0d37a"/>

<br/><br/>
In the final part of the video, the fireflies captured by your hand movements gather at the center of the screen and form a flame, symbolizing Yoon Dong-ju's spirit. Then, stars resembling a pen appear, followed by the lyrics of the song.

<img width="60%" src="https://github.com/DIYongSeok/interactive-video-using-hand-tracking/assets/146920174/3791b4c6-627c-4d74-80ca-79d4de8108ba"/>


## To Start
1. Check the requirements below.

-  Requirements
    - [processing](https://processing.org/download)
    - [anaconda](https://www.anaconda.com/download)
    - webcam

2. Download this project and set up a virtual environment for python server.

    ```sh
    git clone https://github.com/DIYongSeok/interactive-video-using-hand-tracking.git
    cd interactive-video-using-hand-tracking/
    conda env create -f environment.yml
    conda activate hand-track
    cd hand-tracking/
    ```
3. (optional) check the available camera number running 'test-available-cam.py'. This will show a list of the number of available cam in your computer.

    ```sh
    python test-available-cam.py
    ```

4. Launch the server. If you have a specific cam number, put the number using '--cam_id'

    ```sh
    python hand-track.py

    or
    
    python hand-track.py --cam_id (the number of your webcam)

5. Launch the processing and download the libraries list below.
    > go to [`sketch` -> `manage libraries...`] and search the libraries

    - minim
    - opencv
    - video library for processing 4

6. For copyright issues, please download the files (music, font) yourself. Place them in the appropriate folders as specified below.

    - [YoonDong-ju.ttf](https://gscaltexmediahub.com/esg/the-energy-of-independence-fighters-2/) > /processing-code/data/font
    - [당신의 밤 (feat. 오혁)/황광희 X 개코](https://www.ssyoutube.com/watch?v=kZWiF-x3tzg/) > /processing-code/data/music

    > When you download the music mentioned above, it will be in '.mp4' format, a video format. You need to convert it to '.mp3' format using [this site](https://convertio.co/) or any suitable software.


7. Go to `processing-code` folder and open `main.pde`. Finally, press the button located at the top left corner (usually a play button) to start the project.