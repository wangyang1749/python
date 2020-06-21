import numpy as np
import cv2

print('opencv',cv2.__version__)
img = np.zeros((3,3),dtype=np.uint8)

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('myWindow')
cv2.setMouseCallback('myWindow',onMouse)

success,frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('myWindow',frame)
    success, frame = cameraCapture.read()

cv2.destroyAllWindows('myWindow')
cameraCapture.release()