import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)  # This gives the video time to load

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting all the pixels to gray
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My videos", gray_frame_gau)  # Showing the video

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()