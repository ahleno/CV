import cv2
import numpy as np

# 0을 누르면 원본
# 1을 누르면 Roberts
# 2를 누르면 Prewitt
# 3을 누르면 Sobel
# 4 laplacian

roberts = False
prewitt = False
sobel = False
laplacian = False

## roberts
roberts_X = np.array([[0, 0, -1],
                      [0, 1,  0],
                      [0, 0,  0]])
roberts_Y = np.array([[-1, 0, 0],
                      [ 0, 1, 0],
                      [ 0, 0, 0]])

## prewitt
prewitt_X = np.array([[1, 0, -1],
                      [1, 0, -1],
                      [1, 0, -1]])
prewitt_Y = np.array([[-1, -1, -1],
                      [ 0,  0, 0],
                      [ 1,  1, 1]])

capture = cv2.VideoCapture(0) 

if (capture.isOpened() == False) :
    print('Error')

while(True):
    ret, frame = capture.read()
    
    if ret :
        org = frame.copy()
        
        if roberts == True:
            frame = cv2.convertScaleAbs(cv2.filter2D(frame, -1, roberts_X))
        
        elif prewitt == True:
            frame = cv2.convertScaleAbs(cv2.filter2D(frame, -1, prewitt_X))
        
        elif sobel == True:
            frame = cv2.Sobel(frame, cv2.CV_8U, 1, 1, ksize = 3)  

        elif laplacian == True:
            frame = cv2.Laplacian(frame, cv2.CV_8U, ksize = 3)  
        
        else :
            frame = org
        
        cv2.imshow('Frame', frame)
        
        
        key = cv2.waitKey(32)
        
        if key == ord('s') :
            break
        
        elif key == ord('0') :
            # original
            roberts = False
            prewitt = False
            sobel = False
            laplacian = False
            
        elif key == ord('1') :
            # roberts
            roberts = True
            prewitt = False
            sobel = False
            laplacian = False
            
        elif key == ord('2') :
            # prewitt
            roberts = False
            prewitt = True
            sobel = False
            laplacian = False            
            
        elif key == ord('3') :
            # sobel
            roberts = False
            prewitt = False
            sobel = True
            laplacian = False            
            
        elif key == ord('4') :
            # laplacian
            roberts = False
            prewitt = False
            sobel = False
            laplacian = True                     
                     
        
    else : 
        break    
            
        
capture.release()
cv2.destroyAllWindows()
