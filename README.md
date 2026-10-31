# Human Pose Estimation with YOLOv8

## About the Project

This project explores human pose estimation using YOLOv8 and OpenCV. The main aim is to detect human body keypoints from a dance video and visualize the human skeleton.

I used a pretrained YOLOv8 Pose model to process the video frame by frame and generate a separate output video showing the detected body joints on a black background.

## Technologies Used

* Python
* YOLOv8 Pose
* OpenCV
* NumPy
* Google Colab

## Project Features

* Human pose detection from videos.
* Detection of 17 body keypoints.
* Human skeleton visualization.
* Video processing frame by frame.
* Generation of an output pose video.

## Project Files

* `pose_detection.py` – Main Python implementation.
* `dance_pose_colab.ipynb` – Google Colab notebook.
* `dance_pose_colab` – Complete execution workflow.
* `requirements.txt` – Required Python libraries.
* `pose_video.mp4` – Generated output video.

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

1. Open the Google Colab notebook.
2. Install the required libraries.
3. Upload a dance video.
4. Load the YOLOv8 Pose model.
5. Run the pose estimation code.
6. Download the generated `pose_video.mp4`.

## Model

The project uses the pretrained `yolov8n-pose.pt` model.

## Output

The output video displays detected human body keypoints and skeleton connections on a black background.

## Conclusion

Through this project, I explored how computer vision can be used to identify human body positions and visualize movement using deep learning.
