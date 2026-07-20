import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("spider-man.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(gray , cmap = 'gray')
plt.title("RGB Image")
plt.axis("off")
plt.show()