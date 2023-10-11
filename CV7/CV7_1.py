import cv2

g_image = cv2.imread('img/Lena_256g.bmp', cv2.IMREAD_GRAYSCALE)

while True:
    
    cv2.imshow('Image', g_image)

    key = cv2.waitKey(0)
    
    if key == ord('a'):
        g_image = cv2.add(g_image, 10)
    elif key == ord('s'):
        g_image = cv2.subtract(g_image, 10)
    else:
        break