import cv2
from detector import detect_objects

def track_objects(path):
    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_objects(frame)

        for box in detections:
            x1, y1, x2, y2, label = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
