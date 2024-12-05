import os
import platform

def open_video_file():
    video_file = "abc.mp4"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", video_file)
    
    if not os.path.exists(desktop_path):
        print(f"File not found: {desktop_path}")
        return
    os.startfile(desktop_path)
    print(f"Opening video file: {desktop_path}")

open_video_file()
