import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    
    ret, frame = capture.read()
    if not ret:
        break

    # 분리
    (b, g, r) = cv2.split(frame)
    
    # 병합
    merge_img = cv2.merge((b, g, r))

    cv2.imshow("Frame", frame)
    
    cv2.imshow("R", b)
    cv2.imshow("G", g)
    cv2.imshow("B", r)
    
    cv2.imshow("Merged Image", merge_img)

    if cv2.waitKey(32) > 0:
        break
    
capture.release()