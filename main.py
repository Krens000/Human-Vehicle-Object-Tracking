import cv2
from ultralytics import YOLO

# Paths
VIDEO_PATH = "media/videos/your_video.mp4"  # Replace with your filename
MODEL_PATH = "models/yolov8n.pt"            # Replace with your YOLO model

# Define class IDs for humans and vehicles
# COCO class IDs: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml
TARGET_CLASSES = {
    0: "person",
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
    1: "bicycle"
}

# Colors for each class (BGR)
COLORS = {
    "person": (0, 255, 0),
    "car": (0, 0, 255),
    "motorcycle": (255, 0, 0),
    "bus": (255, 255, 0),
    "truck": (0, 255, 255),
    "bicycle": (255, 0, 255)
}

def main():
    # Load YOLOv8 model
    model = YOLO(MODEL_PATH)

    # Load video
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("❌ Error: Cannot open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run detection
        results = model(frame)[0]

        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            if cls_id in TARGET_CLASSES:
                label = f"{TARGET_CLASSES[cls_id]} {conf:.2f}"
                color = COLORS[TARGET_CLASSES[cls_id]]
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

        # Show the frame
        cv2.imshow("YOLOv8: Human + Vehicle Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
