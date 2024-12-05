import time
import os

def simulate_video_process(video_path):
    try:
        print("Process started. Please wait...")
        
        time.sleep(2)

        print("Extracting news...")
        time.sleep(5)  

        print("Converting to speech...")
        time.sleep(8)  
        print("Generating video...")
        time.sleep(15) 

        print("Opening video file...")
        os.startfile(video_path) if os.name == 'nt' else os.system(f'open "{video_path}"')

    except FileNotFoundError:
        print(f"Error: The file {video_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

video_file_path = r"C:\Users\KIIT\Desktop\abcd.mp4"  

simulate_video_process(video_file_path)
