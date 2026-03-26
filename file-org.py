import os
import shutil
from datetime import datetime

SOURCE_DIR = "/home/bayo/Downloads"
LOG_FILE = "organizer.log"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"]
}

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

log_message("Organizer started")

for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(SOURCE_DIR, folder)
                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, folder_path)
                print(f"Moved {filename} → {folder}")
                log_message(f"Moved {filename} to {folder}")

                moved = True
                break

        if not moved:
            other_path = os.path.join(SOURCE_DIR, "Others")
            os.makedirs(other_path, exist_ok=True)

            shutil.move(file_path, other_path)
            print(f"Moved {filename} → Others")
            log_message(f"Moved {filename} to Others")

log_message("Organizer finished")
