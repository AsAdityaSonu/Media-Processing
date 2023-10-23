import time
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands  
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for ids, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = frame.shape  # height, width and channel
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(ids, cx, cy)
                if ids == 4:
                    cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)

            # mpDraw.draw_landmarks(frame, handLms) for dots only.
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
