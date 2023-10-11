# 공간 필터링
# Merge를 통해 원본 + 원본 또는 원본 + 필터영상 출력
# 사용자 입력 0~4 까지 받아 그에 따른 필터링 수행
# 키보드 매핑
# 0: 원본
# 1: 가우시안 블러링
# 2: 중간값 필터링
# 3: 샤프닝
# 4: 언샵마스크

import cv2
import numpy as np

#Define
origin = True
gaussian = False
median = False
sharpening = False
unsharp = False

s_mask = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

cap = cv2.VideoCapture(0) 
   
if (cap.isOpened() == False):  
    print("Error reading video file") 

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
   
size = (frame_width * 2, frame_height) 
   
video = cv2.VideoWriter('capture.mp4',  
                         cv2.VideoWriter_fourcc(*'mp4v'), 
                         30, size, isColor=False) 
    
while(True): 
    ret, frame = cap.read() 
  
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    if ret == True:
        
        if origin:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(tmp)
        
        if gaussian:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.GaussianBlur(tmp, (11, 11), 3))
            
        if median:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.medianBlur(tmp, 9))
            
        if sharpening:
            tmp = frame.copy()
            copy = cv2.convertScaleAbs(cv2.filter2D(tmp, -1, s_mask))
            
        if unsharp:
            tmp = frame.copy()
            blur = cv2.GaussianBlur(tmp, (0, 0), 3)
            copy = cv2.convertScaleAbs(np.clip(2.*tmp-blur, 0, 255).astype(np.uint8))
        
        merged = np.hstack((frame, copy))

        video.write(merged) 
  
        cv2.imshow('Merge', merged) 
        
        key = cv2.waitKey(32)
        
        if key == ord('s'):            
            break
        elif key == ord('0'): # 원본
            origin = True
            gaussian = False
            median = False
            sharpening = False
            unsharp = False
        elif key == ord('1'): # 가우시안
            origin = False
            gaussian = True
            median = False
            sharpening = False
            unsharp = False
        elif key == ord('2'): # 중간값
            origin = False
            gaussian = False
            median = True
            sharpening = False
            unsharp = False
        elif key == ord('3'): # 샤프닝
            origin = False
            gaussian = False
            median = False
            sharpening = True
            unsharp = False
        elif key == ord('4'): # 언샵
            origin = False
            gaussian = False
            median = False
            sharpening = False
            unsharp = True
        
    else: 
        break
  

cap.release() 
video.release() 
    
cv2.destroyAllWindows() 
   
print("The video was successfully saved") 