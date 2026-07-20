import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bat-man.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")
plt.show()