import cv2

cap = cv2.VideoCapture(0)  # (Camera Number)

while True:
    ret, frame = cap.read()  # return 2 values

    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # print(frame)  #will return matrix of image captured by camera
    # print(ret)    #will return true until camera is on

    cv2.imshow('frame', frame)  # (windows name, matrix)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # if cv2.waitKey(1) & 0xFF == ord('q') checks if the key pressed is 'q'.
        break

cap.release()
cv2.destroyAllWindows()
