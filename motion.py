import cv2

# 카메라 모듈 초기화
cap = cv2.VideoCapture(0)  # 0은 내장 카메라를 의미합니다. 만약 외부 카메라를 사용하려면 인덱스를 바꿔주세요.

# 송출할 윈도우 생성
cv2.namedWindow("Live Video", cv2.WINDOW_NORMAL)

while True:
    # 비디오에서 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽혔는지 확인
    if not ret:
        break

    # 프레임을 화면에 표시
    cv2.imshow("Live Video", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 작업
cap.release()
cv2.destroyAllWindows()
