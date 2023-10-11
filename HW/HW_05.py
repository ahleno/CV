# 에지 검출
# Merge를 통해 원본 + 원본 또는 원본 + 필터영상 출력
# 사용자 입력 0~4 까지의 값을 통해 적용할 필터 변경
# 키보드 매핑
# 0: 원본
# 1: 프리윗(Prewitt) : Magnitude 출력
# 2: 소벨 : Magnitude 출력
# 3: 라플라시안 
# 4: 캐니(Canny)

import cv2
import numpy as np

origin = True
prewitt = False
sobel = False
laplacian = False
canny = False

prewitt_Y = np.array([[-1, -1, -1],
                      [ 0,  0, 0],
                      [ 1,  1, 1]])

cap = cv2.VideoCapture(0) 
   
if (cap.isOpened() == False):  
    print("Error reading video file") 

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
   
size = (frame_width * 2, frame_height) 
   
video = cv2.VideoWriter('capture2.mp4',  
                         cv2.VideoWriter_fourcc(*'mp4v'), 
                         30, size, isColor=False) 

while(True): 
    ret, frame = cap.read() 
  
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    if ret == True:
        
        if origin:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(tmp)
        
        if prewitt:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.filter2D(tmp, -1, prewitt_Y))
            
        if sobel:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.Sobel(tmp, cv2.CV_8U, 1, 1, ksize = 3))
            
        if laplacian:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.Laplacian(tmp, cv2.CV_8U, ksize = 3))
            
        if canny:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.Canny(tmp, 150, 300))
        
        merged = np.hstack((frame, copy))

        video.write(merged) 
  
        cv2.imshow('Merge', merged) 
        
        key = cv2.waitKey(32)
        
        if key == ord('s'):            
            break
        elif key == ord('0'): # 원본
            origin = True
            prewitt = False
            sobel = False
            laplacian = False
            canny = False
        elif key == ord('1'): # 가우시안
            origin = False
            prewitt = True
            sobel = False
            laplacian = False
            canny = False
        elif key == ord('2'): # 중간값
            origin = False
            prewitt = False
            sobel = True
            laplacian = False
            canny = False
        elif key == ord('3'): # 샤프닝
            origin = False
            prewitt = False
            sobel = False
            laplacian = True
            canny = False
        elif key == ord('4'): # 언샵
            origin = False
            prewitt = False
            sobel = False
            laplacian = False
            canny = True
        
    else: 
        break
  

cap.release() 
video.release() 
    
cv2.destroyAllWindows() 
   
print("The video was successfully saved") 