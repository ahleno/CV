import cv2
import datetime

capture = cv2.VideoCapture(0)

while capture.isOpened():
    
    ret, frame = capture.read()
    
    if not ret:
        break
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(32)
    
    if key == ord('x'):
        break
    
    elif key == ord('s'):
        current_time = datetime.datetime.now()
        fname = 'img/{}-{}-{}.jpg'.format(current_time.hour, current_time.minute, current_time.second)
        cv2.imwrite(fname, frame)

capture.release()