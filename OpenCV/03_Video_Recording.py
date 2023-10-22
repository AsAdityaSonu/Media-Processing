# Saving data
import cv2

cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30, (680, 420))  # (filename, fourcc code, frame, (size AXB))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
