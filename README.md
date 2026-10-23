# Pipeline Crack Detection Using OpenCV

## Description
Real-time pipeline surface inspection using an IP camera
and traditional OpenCV image processing.

## Technologies
- Python 3
- OpenCV
- NumPy
- IP Camera

## Features
- Real-time camera feed
- Grayscale conversion
- CLAHE contrast enhancement
- Canny edge detection
- Morphological processing
- Contour-based candidate detection

## Setup
Install dependencies:

sudo apt update
sudo apt install python3 python3-pip python3-venv python3-opencv

## Camera Configuration
Edit crack_detection.py and replace CAMERA_URL with
your actual IP camera stream URL.

## Run
python3 crack_detection.py

Press Q to exit.
