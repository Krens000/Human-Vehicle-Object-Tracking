import cv2
from detection.detector import detect_objects

def track_objects(path=0):
    """
    Track objects in:
    - Webcam (default 0)
    - Video file (path="media/videos/vehicle1.mp4")
    - Image file (path="media/images/sample.jpg")
    """
    # If path is an image
    if isinstance(path, str) and path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        frame = cv2.imread(path)
        detections = detect_objects(frame)

        for x1, y1, x2, y2, label, conf in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Image Detection", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return

    # Else assume video/webcam
    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_objects(frame)

        for x1, y1, x2, y2, label, conf in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
