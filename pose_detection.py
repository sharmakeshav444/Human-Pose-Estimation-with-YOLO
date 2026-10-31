from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path

# Input and output paths
INPUT_VIDEO = "dance.mp4"
OUTPUT_VIDEO = "pose_video.mp4"
MODEL_NAME = "yolov8n-pose.pt"

def main():
    # Load the YOLOv8 pose model (downloads weights automatically if needed)
    model = YOLO(MODEL_NAME)
    print("YOLO Pose Model Loaded Successfully!")

    input_path = Path(INPUT_VIDEO)
    if not input_path.exists():
        raise FileNotFoundError(
            f"Cannot find {INPUT_VIDEO}. Put the video in the same folder as this script."
        )

    cap = cv2.VideoCapture(str(input_path))
    if not cap.isOpened():
        raise RuntimeError("Could not open input video. Try another MP4 file.")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25.0

    # Use the original video's dimensions and frame rate
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

    if not out.isOpened():
        cap.release()
        raise RuntimeError("Could not create output video.")

    frame_count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model.predict(frame, conf=0.25, verbose=False)

            # Draw pose keypoints/skeleton on a black background
            black_background = np.zeros_like(frame)
            annotated = results[0].plot(
                img=black_background,
                boxes=False,
                labels=False
            )

            out.write(annotated)
            frame_count += 1

            if frame_count % 30 == 0:
                print(f"Processed {frame_count} frames...")

    finally:
        cap.release()
        out.release()

    if frame_count == 0:
        raise RuntimeError("No frames were read from the input video.")

    print(f"Done! Processed {frame_count} frames.")
    print(f"Output saved to: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
