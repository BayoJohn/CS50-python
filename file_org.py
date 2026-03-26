import os
import shutil

# Folder you want to organize
SOURCE_DIR = "/home/bayo/Downloads"   # change this if needed

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx",".srt",".zip"],
    "Music": [".mp3", ".wav"]
}

for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    if os.path.isfile(file_path):
        for folder, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(SOURCE_DIR, folder)

                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                break
