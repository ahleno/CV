import cv2 

def subplot_frame(frame, num_divisions): 
    h, w, ch = frame.shape

    div_h = int(h / num_divisions)
    div_w = int(w / num_divisions)

    subplot = cv2.resize(frame, (div_w, div_h), cv2.INTER_AREA)

    row = subplot.copy()
    
    for _ in range(num_divisions - 1):
        row = cv2.hconcat([row, subplot])

    final_frame = row.copy()

    for _ in range(num_divisions - 1):
        final_frame = cv2.vconcat([final_frame, row])
     
    final_frame = cv2.resize(final_frame, (w, h))
     
    return final_frame

cap = cv2.VideoCapture(0) 
   

if (cap.isOpened() == False):  
    print("Error reading video file") 
  

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
   
size = (frame_width, frame_height) 
   
video = cv2.VideoWriter('filename.mp4',  
                         cv2.VideoWriter_fourcc(*'mp4v'), 
                         30, size) 
    
num_divisions = 1    

frames_captured = 1
    
while(True): 
    ret, frame = cap.read() 
  
    if ret == True:  

        frame = subplot_frame(frame, num_divisions)

        video.write(frame) 
  
        cv2.imshow('Frame', frame) 
        
        if (num_divisions < 10 and (frames_captured % 60) == 0):
            num_divisions += 1
        
        frames_captured += 1
        
        print(num_divisions)
        
        if num_divisions == 10:
            break
            
        if cv2.waitKey(1) & 0xFF == ord('s'): 
            break
        
    else: 
        break
  

cap.release() 
video.release() 
    
cv2.destroyAllWindows() 
   
print("The video was successfully saved") 