import random
import time
from serial import Serial
import matplotlib.pyplot as plt

# 아두이노가 연결된 포트와 통신 속도 설정
arduino_port = '/dev/tty.usbmodem1101'  # Windows의 경우 (포트 번호에 맞게 수정)
# arduino_port = '/dev/ttyUSB0'  # Linux의 경우
baud_rate = 9600

# 시리얼 포트 열기
ser = Serial(arduino_port, baud_rate)
time.sleep(2)  # 아두이노와 연결될 시간을 주기 위한 대기 시간

# 좌표 설정 (미리 지정된 좌표들)
coordinates = [[2.5, 3], [4.5, 2], [7, 2.5], [3, 10.5], [8, 10.5], 
               [2.5, 16], [5.5, 16], [9,16], [2.5, 18], [9, 18]]

# 플롯 설정
plt.ion()  # interactive mode on
fig, ax = plt.subplots()

# 좌표평면의 기본 설정
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)

try:
    while True:
        if ser.in_waiting > 0:
            # 아두이노로부터 수신한 데이터 읽기
            data = ser.readline().decode('utf-8').rstrip()  # 줄바꿈 문자 제거
            
            # 콤마로 분리하여 6개의 변수로 나누기
            points = data.split(',')
            if len(points) == 6:
                point1 = int(points[0])
                point2 = int(points[1])
                point3 = int(points[2])
                point4 = int(points[3])
                point5 = int(points[4])
                point6 = int(points[5])
                
                # 좌표에 대응하는 숫자를 텍스트로 표시
                ax.clear()
                ax.set_xlim(0, 10)
                ax.set_ylim(0, 20)
                
                ax.text(*coordinates[point1], f"{point1}", fontsize=12, ha='center', color='red')
                ax.text(*coordinates[point2], f"{point2}", fontsize=12, ha='center', color='blue')
                ax.text(*coordinates[point3], f"{point3}", fontsize=12, ha='center', color='green')
                ax.text(*coordinates[point4], f"{point4}", fontsize=12, ha='center', color='orange')
                ax.text(*coordinates[point5], f"{point5}", fontsize=12, ha='center', color='purple')
                ax.text(*coordinates[point6], f"{point6}", fontsize=12, ha='center', color='black')
                
                plt.draw()
                plt.pause(0.1)  # 짧은 대기 시간 후 업데이트

except KeyboardInterrupt:
    print("Terminating the program.")
finally:
    ser.close()  # 시리얼 포트 닫기
