# -*- coding: utf-8 -*-
"""amirthacudaproject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F-Qvn_kti21jdyz5QwLxXJhcXelJdDFv
"""

!nvidia-smi

! pip install pycuda opencv-python

from google.colab import files
uploaded = files.upload()

import cv2
import os
import numpy as np
import time
from matplotlib import pyplot as plt
from PIL import Image

output_dir = "/content/movement_frames"
os.makedirs(output_dir,exist_ok=True)

video_path = "footage.mp4"  # Change if your file name is different
cap = cv2.VideoCapture(video_path)

ret, prev_frame = cap.read()
frame_id = 0
saved_frames = 0

if not ret:
    print(" Error reading the video.")
else:
    start_time = time.time()  # ⏱️ Start timing

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Difference between current and previous frame
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        movement_score = np.sum(thresh) / 255  # Number of changed pixels

        # Threshold for movement detection
        if movement_score > 500:
            save_path = f"{output_dir}/frame_{frame_id:04d}.jpg"
            cv2.imwrite(save_path, frame)
            saved_frames += 1

        prev_gray = gray.copy()
        frame_id += 1

    cap.release()

    end_time = time.time()  # ⏱️ End timing
    total_time = end_time - start_time

    print(f" Extracted {saved_frames} movement frames out of {frame_id} total frames.")
    print(f" Time taken to process video: {total_time:.4f} seconds.")

    video_path = "footage.mp4"  # Change if your file name is different
cap = cv2.VideoCapture(video_path)

ret, prev_frame = cap.read()
frame_id = 0
saved_frames = 0

if not ret:
    print(" Error reading the video.")
else:
    start_time = time.time()  # ⏱️ Start timing

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Difference between current and previous frame
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        movement_score = np.sum(thresh) / 255  # Number of changed pixels

        # Threshold for movement detection
        if movement_score > 500:
            save_path = f"{output_dir}/frame_{frame_id:04d}.jpg"
            cv2.imwrite(save_path, frame)
            saved_frames += 1

        prev_gray = gray.copy()
        frame_id += 1

    cap.release()

    end_time = time.time()  # ⏱️ End timing
    total_time = end_time - start_time

    print(f"Extracted {saved_frames} movement frames out of {frame_id} total frames.")
    print(f" Time taken to process video: {total_time:.4f} seconds.")

import glob
image_files = sorted(glob.glob(f"{output_dir}/*.jpg"))[:3]
for path in image_files:
    img = Image.open(path)
    display(img)

!zip -r movement_frames.zip movement_frames
files.download("movement_frames.zip")

