import cv2

def onMouse(event, x, y, flags, param):
    print(event, x, y)

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(param, (x, y), 30, (255, 0, 0), -1)
        cv2.imshow("Image", param)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param, (x, y), 30, (0, 0, 255), -1)
        cv2.imshow("Image", param)


image = cv2.imread('img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow("Image", image)

cv2.setMouseCallback("Image", onMouse, image)

cv2.waitKey(0)

cv2.destroyAllWindows()