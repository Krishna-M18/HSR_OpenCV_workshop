import cv2
img = cv2.imread("bat-man.jpg")
resized_img = cv2.resize(img, (300, 240))

cv2.imshow("Image",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()