import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 새로운 플롯 설정
fig, ax = plt.subplots()

# 밑창 외곽선을 그리기 위한 좌표 설정
sole_outline = patches.Ellipse((5, 15), width=10, height=30, fill=False, edgecolor='black', lw=2)

# 격자를 그리기 위한 사각형들 추가 (사각형 좌표 및 크기 설정)
rects = [
    patches.Rectangle((2, 25), 6, 3, edgecolor='black', facecolor='black'),  # 윗쪽 부분
    patches.Rectangle((2, 20), 6, 4, edgecolor='black', facecolor='black'),  # 중간 부분
    patches.Rectangle((2, 15), 6, 4, edgecolor='black', facecolor='black'),  # 중간 부분
    patches.Rectangle((2, 10), 6, 4, edgecolor='black', facecolor='black'),  # 중간 부분
    patches.Rectangle((2, 5), 6, 4, edgecolor='black', facecolor='black'),   # 아랫 부분
    patches.Rectangle((2, 2), 6, 3, edgecolor='black', facecolor='black')    # 아랫 부분
]

# 도형을 플롯에 추가
ax.add_patch(sole_outline)
for rect in rects:
    ax.add_patch(rect)

# 축 크기와 비율 설정
ax.set_xlim(0, 10)
ax.set_ylim(0, 30)
ax.set_aspect('equal')

# 플롯 출력
plt.show()
