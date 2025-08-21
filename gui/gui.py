import tkinter as tk
from tkinter import filedialog
from tracking.tracker import track_objects

def launch_gui():
    def open_file():
        file_path = filedialog.askopenfilename()
        track_objects(file_path)

    root = tk.Tk()
    root.title("Vehicle & Human Tracker")

    btn = tk.Button(root, text="Select Video/Image", command=open_file)
    btn.pack(pady=20)

    root.mainloop()
