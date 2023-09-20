import cv2

mouseDown = False

def onMouse(event, x, y, flags, param):
    global mouseDown

    if event == cv2.EVENT_LBUTTONDOWN:
        mouseDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        mouseDown = False
    elif event == cv2.EVENT_LBUTTONDOWN and mouseDown == True:
        cv2.circle(param, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow("Image", param)

image = cv2.imread('img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow("Image", image)

cv2.setMouseCallback("Image", onMouse, image)

cv2.waitKey(0)

cv2.destroyAllWindows()