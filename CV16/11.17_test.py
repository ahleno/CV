import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

while cap.isOpened():
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Hough transform
    
    frame = cv2.blur(frame, (5,5)) # 노이즈 제거
    e_frame = cv2.Canny(frame, 50, 150, apertureSize=3) # Canny 엣지 검출
    
    lines = cv2.HoughLines(e_frame, 1, np.pi/180, 100)
    scale = frame.shape[0] + frame.shape[1]
    
    for line in lines:
        rho, theta = line[0]

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + scale*(-b))
        y1 = int(y0 + scale*(a))
        x2 = int(x0 - scale*(-b))
        y2 = int(y0 - scale*(a))

        cv2.line(frame, (x1,y1), (x2,y2), (255,0,255), 1)
    
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(32) >= 0:
        break
    
cap.release()

