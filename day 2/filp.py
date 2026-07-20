import cv2
import matplotlib.pyplot as plt

img = cv2.imread("bat-man.jpg")
horizontal = cv2.flip(img,1)
vertical = cv2.flip(img,0)
both = cv2.flip(img,-1)

plt.figure(figsize=(20,5))

plt.subplot(1,4,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1,4,2)
plt.imshow(cv2.cvtColor(horizontal, cv2.COLOR_BGR2RGB))
plt.title("Horizontal")

plt.subplot(1,4,3)
plt.imshow(cv2.cvtColor(vertical, cv2.COLOR_BGR2RGB))
plt.title("Vertical")

plt.subplot(1,4,4)
plt.imshow(cv2.cvtColor(both, cv2.COLOR_BGR2RGB))
plt.title("Both")

plt.show()