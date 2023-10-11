import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30.0  # 프레임 속도
frame_width = 640
frame_height = 480
video = cv2.VideoWriter('capture.mp4', fourcc, fps, (frame_width, frame_height))

while cv2.waitKey(32) < 0:

    ret, frame = capture.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)

    video.write(frame)
capture.release()
video.release()