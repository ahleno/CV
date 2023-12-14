import numpy as np
from sklearn.cluster import KMeans

# 주어진 동전 반지름 데이터
coin_data = [
    [54, 55, 55, 55, 64, 64, 66, 70, 71, 73, 74, 78, 81, 83]
]

# NumPy 배열로 변환
X = np.array(coin_data).reshape(-1, 1)

# K-means 모델 생성 (4개의 군집으로 설정)
kmeans = KMeans(n_clusters=4, random_state=42)

# 모델 학습
kmeans.fit(X)

# 각 데이터 포인트의 군집 레이블 얻기
labels = kmeans.labels_

# 군집화 결과 출력
for i, label in enumerate(labels):
    print(f"동전 {i + 1}: 군집 {label + 1}")
