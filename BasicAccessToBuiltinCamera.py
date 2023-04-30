import cv2

# Open a connection to the camera
camera = cv2.VideoCapture(0)

# Set the camera's resolution
camera.set(3, 640)
camera.set(4, 480)

# Continuously capture and display video frames
while True:
    ret, frame = camera.read()
    cv2.imshow("Live Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
