import cv2
import mediapipe as mp
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cam_id', type=int, default=0)
parser.add_argument('--cam_width', type=int, default=1280)
parser.add_argument('--cam_height', type=int, default=720)
args = parser.parse_args()

# 소켓 초기화 함수
def initialize_socket():
    HOST = '127.0.0.1'
    PORT = 3030
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    return s

# Mediapipe 손 인식 모델 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# 웹캠 캡처 객체 생성
cap = cv2.VideoCapture(args.cam_id)
cap.set(3, args.cam_width)
cap.set(4, args.cam_height)

def calculate_palm_center(landmarks, width, height):
    # 0, 5, 17번 랜드마크의 좌표를 사용하여 손바닥 중심을 계산
    x = (landmarks[0].x + landmarks[5].x + landmarks[17].x) / 3 * width
    y = (landmarks[0].y + landmarks[5].y + landmarks[17].y) / 3 * height
    return int(x), int(y)

# 소켓 초기화
sProcessing = initialize_socket()
print('Waiting for a connection...')
conn, addr = sProcessing.accept()
print('Connected by', addr)

while True:
    success, image = cap.read()
    if not success:
        print("카메라에서 영상을 읽어올 수 없습니다.")
        break

    # 이미지를 RGB로 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 손 추적 결과
    results = hands.process(image_rgb)

    # 손 추적 결과를 이미지에 그리기
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 손바닥 포인트들 표시
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 손바닥 중심 좌표 가져오기 (랜드마크 0)
            h, w, c = image.shape
            palm_center = calculate_palm_center(hand_landmarks.landmark, w, h)

            # 좌표를 소켓으로 송신
            try:
                data = str(palm_center[0])+','+str(palm_center[1])
                conn.sendall(data.encode('utf-8'))
                #print(palm_center[0], palm_center[1])
            except:
                print("Connection lost")
                break

    # 결과 출력
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

conn.close()

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
sProcessing.close()