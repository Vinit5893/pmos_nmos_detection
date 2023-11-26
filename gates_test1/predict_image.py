import os
import cv2
from ultralytics import YOLO

# Specify the path to the image and model
# IMAGES_DIR = os.path.join('.', 'images')
# image_path = os.path.join(IMAGES_DIR, 'test1.png')

# model_path = os.path.join('.', 'runs', 'detect', 'train2', 'weights', 'last.pt')

# Load the test image
frame = cv2.imread('/home/vinit-linux/yolov8_detection/pmos_nmos/gates_test1/images/test3.jpg')

# # Resize the image to 416x416
# frame = cv2.resize(frame, (416, 416))
# cv2.imshow('frame', frame)
# cv2.waitKey(0)\

# # Resize the image to 416x416


H, W, _ = frame.shape

# Load the YOLO model
model = YOLO('/home/vinit-linux/yolov8_detection/pmos_nmos/gates_test1/runs/detect/train2/weights/last.pt')

threshold = 0

# Process the image
results = model(frame)[0]

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x2), int(y2 + 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        score_str = f"{score:.2f}"
        cv2.putText(frame, f"{score_str}", (int(x1), int(y2 + 30)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Save the annotated image
# output_image_path = os.path.join(IMAGES_DIR, 'annotated_test_image.jpg')
cv2.imwrite('/home/vinit-linux/yolov8_detection/pmos_nmos/gates_test1/images/test3_output.jpg', frame)

print(f"Annotated image saved at: /home/vinit-linux/yolov8_detection/pmos_nmos/gates_test1/images/test3_output.jpg")
