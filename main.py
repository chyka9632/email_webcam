import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)  # This gives the video time to load

while True:
    check, frame = video.read()
    cv2.imshow("My videos", frame)  # Showing the video

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()