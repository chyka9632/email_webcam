import cv2
import time

video = cv2.VideoCapture(0)

check1, frame1 = video.read()
time.sleep(1)  # Adding timer


check2, frame2 = video.read()
time.sleep(1)

check3, frame3 = video.read()
time.sleep(1)


print(frame3)