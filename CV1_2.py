import cv2

image = cv2.imread("C:/Users/ahleno/Pictures/lenna.png", cv2.IMREAD_UNCHANGED)

# cv2.imwrite("C:/Users/ahleno/Pictures/lenna.jpg", image)

print(image.shape)
cv2.imshow("Image", image)

key = cv2.waitKey(0)
print("key {}".format(key))