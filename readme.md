# Vehicle and Human Tracking System

This project is a powerful AI-based tracking system designed for real-time **vehicle**, **human**, and **object** detection and tracking from webcam, video files, or CCTV feeds. It includes bounding boxes, distance estimation, and an interactive GUI.

## 🚀 Features

* Real-time detection of **humans**, **vehicles**, and **objects**
* Simultaneous multi-object tracking
* Bounding boxes for all detections
* Estimated distance from the camera
* GUI interface for easier interaction

## 💻 Requirements

### ✅ Python Version

* **Python 3.10.x** (recommended)

### ✅ Code Editor

* **PyCharm Community or Professional Edition**

### ✅ Hardware

* Windows 11 system
* NVIDIA GeForce RTX 2050 GPU optioal check online for your gpu with libraries run on them or not

### ✅ Libraries (Install via pip)

```bash
pip install opencv-python
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install ultralytics
pip install tkinter
pip install numpy
pip install matplotlib
```

## 📁 File Structure

```
project_root/
├── main.py                     # Entry point of the program
├── gui.py                      # GUI interface
├── tracker.py                  # Object tracking logic
├── detector.py                 # Detection logic (YOLO, etc.)
├── utils/
│   └── helpers.py              # Utility functions
├── media/
│   ├── videos/                 # Test videos
│   └── images/                 # Test images
├── models/                     # YOLO or other model files
├── README.md                   # Project documentation
└── requirements.txt            # Dependency list
```

## 🧠 Models Used

* YOLOv8 for object detection (via `ultralytics`)
* DeepSORT or ByteTrack (optional for tracking)

## 📦 Setup Instructions

```bash
# Clone repo
https://github.com/yourusername/vehicle-human-tracking.git
cd vehicle-human-tracking

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## 📸 Input Sources

* Webcam (default)
* Video file
* Image
* RTSP/CCTV stream (optional)

## 📃 License

MIT License

---

For any issues, contact: mailto: klimbasiya667@rku.ac.in, vsuliya828@rku.ac.in
