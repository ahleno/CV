import numpy as np
import cv2

c_image = cv2.imread('./img/fortlee_512c.bmp', cv2.IMREAD_UNCHANGED)
g_image = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", c_image)

# SIFT 특징 검출
sift_detector = cv2.xfeatures2d.SIFT_create()
print(type(sift_detector))
keypoints, descriptor = sift_detector.detectAndCompute(g_image, None)
print('Keypoint: ', len(keypoints), 'Descriptor: ', descriptor.shape)
print(descriptor)

ov_image = cv2.drawKeypoints(c_image, keypoints, None,
               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("SIFT detector keypoint image", ov_image)

cv2.waitKey(0)