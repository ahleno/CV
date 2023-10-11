import numpy as np
import cv2

capture = cv2.VideoCapture(0)


### Bitplane
# mask = 0x01 << 7 

### Dithering
mask_2x2 = np.array([[0, 128], [192, 64]])
mask_4x4 = np.array([[0, 128, 32, 160], [192, 64, 224, 96], [48, 176, 16, 144], [240, 112, 208, 80]])


gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
### Dithering
for y in range(0, height, 2):
    for x in range(0, width, 2):
      for j in range(2):
          for i in range(2):
            if g_frame[y*j, x*i] > mask_2x2[j, i]:
                g_frame[y*j, x*i] = 255
            else:
                g_frame[y*j, x*i] = 0
                         

cv2.imshow("Frame", frame)
cv2.resizeWindow("Frame", 512, 512)
