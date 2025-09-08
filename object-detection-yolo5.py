import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolo 7 maybe?
model.conf = 0.5
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cv2.namedWindow("YOLOv5 Object Detection", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    frame = results.render()[0]  #first and only frame of the result list

    cv2.imshow("YOLOv5 Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # quit
        break

cap.release()
cv2.destroyAllWindows()
