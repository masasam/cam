import cv2

cam = cv2.VideoCapture(0)
while True:
    _, img = cam.read()
    cv2.imshow('PUSH ENTER KEY', img)
    if cv2.waitKey(1) == 13: break
cam.release()
cv2.destroyAllWindows()
