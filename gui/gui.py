import tkinter as tk
from tkinter import filedialog
from tracking.tracker import track_objects

def run_gui():
    root = tk.Tk()
    root.title("Vehicle & Human Tracker")

    def open_file():
        filepath = filedialog.askopenfilename(
            filetypes=[("Media files", "*.mp4 *.avi *.jpg *.jpeg *.png *.webp")]
        )
        if filepath:
            track_objects(filepath)

    def open_webcam():
        track_objects(0)

    btn1 = tk.Button(root, text="Open File", command=open_file, width=20)
    btn1.pack(pady=10)

    btn2 = tk.Button(root, text="Open Webcam", command=open_webcam, width=20)
    btn2.pack(pady=10)

    root.mainloop()
