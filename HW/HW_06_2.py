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
                
        coins = []

        for i in circles[0, :]:
            # 동전의 반지름
            radius = i[2]
            
            coins.append(radius)

        # 동전 개수와 총 금액 출력
        coin_count = len(circles[0])
        print(f"동전 개수: {coin_count}")

        return coins
    else:
        print("동전을 찾을 수 없습니다.")
        return None

def calc_amount(coins):
    if coins is not None:
        total_amount = 0
        
        coin_10 = []
        coin_50 = []
        coin_100 = []
        coin_500 = []

        rad_max = max(coins)

        for i in range(len(coins)):
            size_ratio = coins[i] / rad_max

            if size_ratio <= 0.717:
                coin_val = 10
            elif 0.71 < size_ratio <= 0.84:
                coin_val = 50
            elif 0.84 < size_ratio <= 0.93:
                coin_val = 100
            else:
                coin_val = 500
                
            
            total_amount += coin_val

        print(f"금액 : {total_amount}원")
    else:
        print("동전을 찾지 못하여 금액을 계산할 수 없습니다.")

# 이미지 파일 경로 입력
image = ["coins_1.jpg", 
         "coins_2.jpg",
         "coins_3.jpg",
         "coins_4.jpg"]

image_path = ["./img/" + image[0],
              "./img/" + image[1],
              "./img/" + image[2],
              "./img/" + image[3]]



# 동전 감지 및 총 금액 계산
# coins = detect_coins(image_path)
# calc_amount(coins)

for i in range(4):
    print(image[i])
    coins = detect_coins(image_path[i])
    calc_amount(coins)