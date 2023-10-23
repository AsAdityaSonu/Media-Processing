import time
import cv2
import mediapipe as mp

class HandTrackingModule:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def process_video(self):
        pTime = 0
        try:
            while True:
                ret, frame = self.cap.read()

                if not ret:
                    print("Error: Could not read frame.")
                    break

                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(frameRGB)

                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for ids, lm in enumerate(handLms.landmark):
                            h, w, c = frame.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            print(ids, cx, cy)

                        self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime

                cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            self.cap.release()
            cv2.destroyAllWindows()

def main():
    hand_tracking = HandTrackingModule()
    hand_tracking.process_video()

if __name__ == "__main__":
    main()
