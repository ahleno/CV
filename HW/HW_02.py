import numpy as np
import cv2

image = cv2.imread('img/18-4-0.jpg', cv2.IMREAD_GRAYSCALE)

### Dithering
mask_2x2 = np.array([[0, 128], [192, 64]])
mask_4x4 = np.array([[0, 128, 32, 160], [192, 64, 224, 96], [48, 176, 16, 144], [240, 112, 208, 80]])

(height, width) = image.shape

img_2x2 = image.copy()   
img_4x4 = image.copy()
    
### Dithering with mask_2x2
for y in range(0, height -1 ,2):
    for x in range(0 ,width -1 ,2):
        block = img_2x2[y:y+2 , x:x+2]
        for j in range(0 ,min (block.shape[0] , mask_2x2.shape[0])):
            for i in range (0,min(block.shape[1] , mask_2x2.shape[1])):
                if block[j,i]>mask_2x2[j,i]:
                    block[j,i]=255 
                else :
                    block[j,i]=0 

### Dithering with mask_4x4
for y in range(0,height -3 ,4):
    for x in range (0,width -3 ,4 ):
        block=img_4x4[y:y+4,x:x+4]
        for j in range( min(block.shape[1] , mask_4x4 .shape[1])):
            for i in range(min(block .shape [1] , mask_4x4 .shape [1])):
                if block[j,i]>mask_4x4[j,i]:
                    block[j,i]=255 
                else :
                    block[j,i]=0 


cv2.imshow("Image", img_2x2)
cv2.imshow("Image2", img_4x4)
cv2.waitKey(0)
