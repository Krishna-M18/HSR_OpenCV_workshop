import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../day 2/spider-man.jpg")

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("../day 2/spider-man.jpg", img)