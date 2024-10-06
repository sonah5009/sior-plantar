from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import eventlet
import serial

ser = serial.Serial('/dev/tty.usbmodem1101', 9600)  # COM 포트와 보드레이트를 설정하세요. (예: 'COM3'는 윈도우에서의 포트)
# 비동기 지원을 위해 eventlet 사용
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 6개의 점을 정의 (예: 발바닥의 특정 지점)
points = [
    {"id": 1, "x": 100, "y": 100},
    {"id": 2, "x": 200, "y": 100},
    {"id": 3, "x": 300, "y": 100},
    {"id": 4, "x": 150, "y": 200},
    {"id": 5, "x": 250, "y": 200},
    {"id": 6, "x": 200, "y": 300},
]

@app.route('/')
def index():
    return render_template('index.html', points=points)

def generate_data():
    while True:
        # 각 점에 랜덤 값 1-100 할당
        data = {point['id']: random.randint(1, 100) for point in points}
        # 클라이언트에 데이터 전송
        socketio.emit('update', data)
        # 0.05초 대기
        socketio.sleep(0.05)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    # 백그라운드에서 데이터 생성
    socketio.start_background_task(generate_data)
    # 서버 시작
    socketio.run(app, host='0.0.0.0', port=5000)
