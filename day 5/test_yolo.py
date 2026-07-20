from ultralytics import YOLO
import cv2
import os

print("=" * 50)
print("Running File :", __file__)
print("Working Dir  :", os.getcwd())
print("=" * 50)

# Load image
image_path = "vk.jpg"
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Cannot find {image_path}")

print("Image Loaded:", img.shape)

# Load model
model = YOLO("yolo26n.pt")
print("Model Loaded Successfully")

# Prediction
results = model(img)

# Print detections
print(results[0].boxes)

# Save output
annotated = results[0].plot()

cv2.imwrite("output_test.jpg", annotated)

print("Output saved as output_test.jpg")

cv2.imshow("YOLO Result", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()