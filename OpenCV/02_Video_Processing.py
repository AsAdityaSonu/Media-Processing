import cv2

cap = cv2.VideoCapture(0)  # (Camera Number)

while True:
    ret, frame = cap.read()

    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # (Source, conversion)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
