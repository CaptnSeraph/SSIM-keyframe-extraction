# Video Keyframe Detection and Extraction

This Python script analyzes an input video and identifies keyframes based on structural similarity index (SSIM) differences between consecutive frames. The identified keyframes are saved in a separate folder named "synth_frames" for further processing with tools like stable diffusion and ebsynth.

## Features

- Frame extraction from input video
- Frame comparison using structural similarity index (SSIM)
- Keyframe identification based on a predefined threshold
- Saving keyframes with dynamic leading zeros based on total number of frames in the input video
- Progress bars for processing frames and saving keyframes

## Dependencies

- Python 3.x
- OpenCV
- scikit-image
- numpy
- tqdm

## Installation

1. Install Python 3.x if not already installed.

2. Clone this repository or download the script.

3. Install the required Python libraries:

```bash
pip install opencv-python-headless scikit-image numpy tqdm
```

## Usage

Edit the INPUT_VIDEO and OUTPUT_PATH constants in the script to specify the input video file and the output directory for saving keyframes.

(Optional) Adjust the FRAME_RATE and THRESHOLD constants to change the frame rate for processing and the threshold for keyframe identification.

Run the script:

```bash
python video_keyframe_detection.py
```

The identified keyframes will be saved in the "synth_frames" folder inside the specified output directory.

## Notes

The script is designed to work with various video lengths and adjusts the leading zeros for saved keyframes dynamically based on the total number of frames in the input video.
This script provides a basic outline for the desired functionality. You will need to set up and integrate stable diffusion and ebsynth tools for further processing of the keyframes

