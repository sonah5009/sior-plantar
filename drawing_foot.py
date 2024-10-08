import matplotlib.pyplot as plt
import matplotlib.patches as patches
"""
matplotlib.patches.Circle( (중심좌표), radius=반지름)

matplotlib.patches.Rectangle( (좌측하단모서리좌표), 가로길이,세로길이)

matplotlib.patches.Ellipse( (중심좌표), 가로,세로, angle=기울임)

matplotlib.pyplot.gca().add_patch(여기에 입력) 
"""
# 새로운 플롯 설정
fig, ax = plt.subplots()

# 밑창 외곽선을 그리기 위한 좌표 설정 - right
sole_outline = patches.Rectangle((0, 0), width=195, height=537, fill=False, edgecolor='black', lw=2)

# 격자를 그리기 위한 사각형들 추가 (사각형 좌표 및 크기 설정)
x_ls = [[87, 134], [87, 134], [69, 109, 146], [27, 69, 107, 147], [27, 69, 116]]
y_ls = [[56, 56], [154, 154], [259, 259, 259], [367, 356, 356, 356], [454, 454, 435]]
sensor_size = 20
foot_w = 196
foot_h = 537 # width, height
plantar_r = []


# 각 좌표에 대해 사각형 패치를 추가
for i in range(len(x_ls)):  # x_ls의 길이만큼 반복
    for j in range(len(x_ls[i])):  # 각 줄의 x 좌표에 맞는 y 좌표들에 대해 반복
        plantar_r.append(patches.Rectangle((x_ls[i][j], y_ls[i][j]), sensor_size, sensor_size, edgecolor='black', fill=False))

# 도형을 플롯에 추가
ax.add_patch(sole_outline)
for r in plantar_r:
    ax.add_patch(r)

# 축 크기와 비율 설정
ax.set_xlim(0, 195)
ax.set_ylim(0, 537)
ax.set_aspect('equal')

# 플롯 출력 - both
plt.xlim(0, 500)
plt.ylim(0, 700)
plt.show()
