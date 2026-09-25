# Real-Time Color Detection

A simple Python project that detects and tracks a specific color (configured for Orange) in real-time using a webcam, then draws a green bounding box around it.

## How it Works
1. **Color Space Conversion:** The webcam frame is converted from BGR to HSV to ensure accurate color isolation regardless of lighting conditions.
2. **Masking:** cv2.inRange creates a binary mask where the target color appears as white and everything else is black.
3. **Bounding Box Localization:** Instead of using complex loops, the mask is converted to a Pillow image object. The getbbox() method instantly finds the exact coordinates of the detected color.
4.. **Motion Smoothing (deque):** A `deque` with `maxlen=5` is used 
   to store the last 5 detected bounding box positions. The average 
   of these positions is calculated to draw a smoother rectangle
5. **Drawing:** OpenCV uses these coordinates to draw a green rectangle on the live video feed.

## Requirements
Make sure you have the following libraries installed:
```bash
pip install numpy opencv-python Pillow

Usage


1-Keep both computer_vision.py and util.py in the same project folder.
2-Run the computer_vision.py script to start the real-time color detection.
3- press 'q' to exit the application.



├── computer_vision.py   # Main script (webcam + detection + smoothing)
├── util.py              # Contains get_limits() for HSV range calculation
└── README.md


