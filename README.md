# Human Pose Estimation with YOLO

## Project Overview

This project implements **Human Pose Estimation** using the Ultralytics YOLO pose-estimation model. It detects human body keypoints from a video and connects them to create a skeletal representation of the human body.

The project processes the input video and generates two different visual outputs:

- **Skeleton Visualization:** Displays the detected human skeleton on a black background.
- **Pose Overlay:** Displays the detected skeleton over the original video.

## Project Files

| File Name | Description |
|---|---|
| `pose_estimation.ipynb` | Jupyter Notebook containing the pose detection and video processing implementation. |
| `input.mp4` | Original video used as input for pose estimation. |
| `pose_output.mp4` | Processed video showing the white human skeleton on a black background. |
| `pose_overlay.mp4` | Processed video displaying the skeleton over the original video. |

## Technologies Used

- Python
- Ultralytics YOLO
- OpenCV
- NumPy
- Jupyter Notebook

## Installation

Make sure Python is installed on your system. Install the required dependencies using:

```bash
python -m pip install ultralytics opencv-python numpy
```

## How to Run the Project

Follow these steps to execute the project:

1. Clone or download this repository.
2. Ensure that `input.mp4` is available in the same directory as the notebook.
3. Download the pretrained `yolo26n-pose.pt` model weights and place them in the project directory.
4. Open `pose_estimation.ipynb` using Jupyter Notebook or JupyterLab.
5. Run the notebook cell to start the pose estimation process.
6. After processing is complete, two output videos will be generated:
   - `pose_output.mp4`
   - `pose_overlay.mp4`

## Output Videos

The project generates the following outputs:

1. **Original Input Video:** The video provided as input.
2. **Pose Overlay:** Shows the detected human keypoints and skeleton connections over the original video.
3. **Skeleton on Black Background:** Displays only the detected human skeleton using white keypoints and connecting lines against a black background.

## Model and Pose Visualization

The project uses the pretrained `yolo26n-pose.pt` model from Ultralytics for human pose estimation.

The model identifies important human body keypoints and connects them using predefined skeleton connections. Keypoints are displayed only when their confidence scores are above **0.25**.

No additional model training or fine-tuning is performed. The project directly uses pretrained model weights to perform pose detection and video visualization.

## Key Features

- Human pose detection from video frames.
- Detection of human body keypoints.
- Skeleton visualization on a black background.
- Skeleton overlay on the original video.
- Confidence-based keypoint filtering.
- Automated video processing and output generation.

## Conclusion

This project demonstrates how computer vision and pretrained YOLO models can be used to detect human body posture and visualize skeletal structures from video. It provides two different visualization methods to make human pose estimation easier to understand and analyze.
