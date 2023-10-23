import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands  # Formality
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # Convert to RGB
    results = hands.process(frameRGB)

    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)     # mpDraw.draw_landmarks(frame, handLms) for dots only.

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
