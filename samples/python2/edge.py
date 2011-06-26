import cv2, cv
import video
import sys

try: fn = sys.argv[1]
except: fn = video.presets['chess']

def nothing(*arg):
    pass

cv2.namedWindow('edge')
cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

cap = video.create_capture(fn)
while True:
    flag, img = cap.read()
    gray = cv2.cvtColor(img, cv.CV_BGR2GRAY)
    thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
    thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
    edge = cv2.canny(gray, thrs1, thrs2, apertureSize=5)
    vis = img.copy()
    vis /= 2
    vis[edge != 0] = (0, 255, 0)
    cv2.imshow('edge', vis)
    ch = cv2.waitKey(5)
    if ch == 27:
        break

