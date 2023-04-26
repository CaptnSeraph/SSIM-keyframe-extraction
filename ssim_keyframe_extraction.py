import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os
from tqdm import tqdm

# Constants
INPUT_VIDEO = 'path/to/input/video'
FRAME_RATE = 1  # Specify your desired frame rate
THRESHOLD = 0.25  # Set the threshold for keyframe identification
OUTPUT_PATH = 'path/to/output/folder'

# Function to calculate the difference between two frames
def calculate_difference(frame1, frame2):
    return ssim(frame1, frame2, multichannel=True)

try:
    # Video Input and frame count
    cap = cv2.VideoCapture(INPUT_VIDEO)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    num_digits = len(str(total_frames))
    cap.release()

    # Frame Extraction, Comparison, and Difference Accumulation
    frame_diffs = []
    prev_frame = None
    frame_count = 0

    cap = cv2.VideoCapture(INPUT_VIDEO)
    with tqdm(total=total_frames, desc="Processing frames") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if prev_frame is not None:
                diff = calculate_difference(gray_frame, prev_frame)
                frame_diffs.append(diff)

            prev_frame = gray_frame
            pbar.update(1)

            if frame_count % FRAME_RATE == 0:
                cv2.waitKey(1000)
    cap.release()

    # Difference Accumulation
    accumulated_diffs = np.cumsum(frame_diffs)

    # Keyframe Identification
    keyframes = [i for i, diff in enumerate(frame_diffs) if diff < THRESHOLD]

    # Save Keyframes in the "synth_frames" folder
    synth_frames_path = os.path.join(OUTPUT_PATH, 'synth_frames')
    os.makedirs(synth_frames_path, exist_ok=True)

    cap = cv2.VideoCapture(INPUT_VIDEO)
    with tqdm(total=len(keyframes), desc="Saving keyframes") as pbar:
        for frame_idx in keyframes:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()

            if ret:
                filename = f"{frame_idx:0{num_digits}d}.png"
                cv2.imwrite(os.path.join(synth_frames_path, filename), frame)

            pbar.update(1)
    cap.release()

except Exception as e:
    print(f"An error occurred: {e}")
    