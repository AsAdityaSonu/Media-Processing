# Read Open img file 
import cv2

img = cv2.imread('Images/Dog.jpg', 0)  # 0 = grayScale, 1= color, -1= unchanged
print(img)  # Matrix Form

cv2.imshow('img', img)
k = cv2.waitKey(5000)  # 5 Seconds, 0 will wait until you close it

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Images/dog_copy.png', img)  # Creates a file named dog_copy.png using data in img
    cv2.destroyAllWindows()
