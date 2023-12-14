import cv2
import numpy as np

def detect_coins(image_path):
    # 이미지 불러오기
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 그레이스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 블러 처리
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # 원 검출을 위한 허프 원 변환 적용
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=50,
        param2=30,
        minRadius=30,
        maxRadius=100
    )

    if circles is not None:
        # 감지된 동전 그리기 및 금액 계산
        circles = np.uint16(np.around(circles))
        total_amount = 0

        # Reference object size (e.g., a coin with a known size)
        reference_object_radius = 100  # Adjust this value based on your reference object

        for i in circles[0, :]:
            # 동전의 반지름
            radius = i[2]

            # 동전의 크기 비율 계산
            size_ratio = radius / reference_object_radius

            # 동전의 금액 할당 (가상의 크기에 따라 조절)
            if size_ratio < 0.75:  # 10원
                coin_value = 10
                print(coin_value, radius)
            elif size_ratio < 0.85:  # 50원
                coin_value = 50
                print(coin_value, radius)
            elif size_ratio < 0.95:  # 100원
                coin_value = 100
                print(coin_value, radius)
            else:  # 500원
                coin_value = 500
                print(coin_value, radius)

            # 총 금액 계산
            total_amount += coin_value

            # 동전 그리기
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)

        # 동전 개수와 총 금액 출력
        coin_count = len(circles[0])
        print(f"동전 개수: {coin_count}")
        print(f"총 금액: {total_amount} 원")

        # 결과 이미지 출력
        cv2.namedWindow("Detected Coins", cv2.WINDOW_NORMAL)
        cv2.imshow("Detected Coins", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("동전을 찾을 수 없습니다.")

# 이미지 파일 경로 입력
image_path = "./img/coins_3.jpg"

# 동전 감지 및 총 금액 계산
detect_coins(image_path)
