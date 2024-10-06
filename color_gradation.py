import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.interpolate import griddata

# 센서 값 생성
point1 = random.randrange(1, 10)
point2 = random.randrange(11, 20)
point3 = random.randrange(21, 30)
point4 = random.randrange(31, 40)
point5 = random.randrange(41, 50)
point6 = random.randrange(51, 60)
points = [point1, point2, point3, point4, point5, point6]

# 좌표 설정
coordinates = [[2.5, 3], [4.5, 2], [7, 2.5], [3, 10.5], [8, 10.5], 
               [2.5, 16], [5.5, 16], [9, 16], [2.5, 18], [9, 18]]

# x, y 좌표 리스트 생성
x_coords = [coord[0] for coord in coordinates[:6]]  # First 6 points only for sensor mapping
y_coords = [coord[1] for coord in coordinates[:6]]

sensor_values = points  # 각 좌표에 매칭되는 센서 값

# 좌표와 축 설정
plt.xlim(0, 10)
plt.ylim(0, 20)

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

plt.ion()  # interactive mode on

while True:
    # 센서 값을 랜덤으로 업데이트
    point1 = random.randrange(1, 10)
    point2 = random.randrange(11, 20)
    point3 = random.randrange(21, 30)
    point4 = random.randrange(31, 40)
    point5 = random.randrange(41, 50)
    point6 = random.randrange(51, 60)
    sensor_values = [point1, point2, point3, point4, point5, point6]

    # 그리드 생성
    grid_x, grid_y = np.mgrid[0:10:100j, 0:20:200j]  # Define a grid

    # 센서 값에 대한 그리드 데이터 보간
    grid_z = griddata((x_coords, y_coords), sensor_values, (grid_x, grid_y), method='linear')

    # 기존 플롯 삭제
    plt.clf()

    # 보간된 데이터로 heatmap 플롯
    plt.imshow(grid_z.T, extent=(0, 10, 0, 20), origin='lower', cmap='jet', alpha=0.7, interpolation='bilinear')

    # 원래 좌표의 포인트에 scatter 플롯을 겹쳐 표현
    plt.scatter(x_coords, y_coords, c=sensor_values, cmap='jet', s=200, edgecolor='k')  # 센서 점 표시
    plt.colorbar(label='Sensor Value')
    
    # 그래프 그리기
    plt.draw()
    plt.pause(0.5)  # 짧은 대기 시간 후 업데이트
