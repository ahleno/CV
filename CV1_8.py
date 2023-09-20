import cv2

image = cv2.imread('img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)

x, y = 100, 100

while True:
    cv2.imshow("Image", image)
    cv2.moveWindow("Image", x, y)
    
    key = cv2.waitKey(0)
    print(f'Key = {key}, Char = {chr(key)}')
    
    if key == ord('j'):
        x -= 3
    elif key == ord('k'):
        x += 3
    elif key == ord('i'):
        y -= 3
    elif key == ord('m'):
        y += 3
    else :
        break