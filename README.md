# Basic Access to Built in camera using OpenCV

## Live Video Display Program

## Introduction
This program uses the OpenCV library to open a connection to a camera and continuously capture and display video frames. The camera's resolution is set to 640x480 by default, but this can be adjusted as needed. The video frames are displayed in a window named "Live Video". The program will continue to run and display video frames until the user presses the 'q' key or 'control c'.

## Requirements
This program requires the OpenCV library to be installed.

## Usage
To use this program, simply run it in a Python environment that has the OpenCV library installed. It will open a connection to the default camera and start displaying video frames in a window named "Live Video". To stop the program, simply press the 'q' key.

## Notes
- If you have multiple cameras connected to your system, you can specify the index of the camera you want to use by changing the argument in `cv2.VideoCapture()` from 0 to the index of the desired camera.
- If you want to adjust the camera's resolution, you can use the `camera.set()` method to set the desired width and height. The values used in this program are 640 and 480, respectively.
- The program will continue to run and display video frames until the user presses the 'q' key. To stop the program, simply press the 'q' key or 'control c'.
- Once the program is stopped, be sure to release the camera and close the window by calling `camera.release()` and `cv2.destroyAllWindows()`, respectively. This will ensure that the camera is properly released and the window is closed.
