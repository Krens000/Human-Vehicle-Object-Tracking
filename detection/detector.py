from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pretrained on COCO dataset)
model = YOLO("yolov8n.pt")  # Small model for speed

def detect_objects(frame):
    """
    Run object detection on a frame.
    Returns list of detections: (x1, y1, x2, y2, label, confidence)
    """
    results = model.predict(frame, verbose=False)

    detections = []
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            detections.append((int(x1), int(y1), int(x2), int(y2), label, conf))

    return detections
