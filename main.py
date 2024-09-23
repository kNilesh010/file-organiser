import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
  ".png": "Image",
  ".jpg": "Image",
  ".jpeg": "Image",
  ".gif": "Image",
  ".HEIC": "Image",
  ".zip": "Archived",
  ".mp4": "Video",
  ".mov": "Video",
  ".txt": "Documents",
  ".pdf": "Documents",
  ".xls": "Documents",
  ".mp3": "Music",
  ".wav": "Music",
}

for filename in os.listdir(directory):
  file_path = os.path.join(directory, filename)
  
  if os.path.isfile(file_path):
    extension = os.path.splitext(filename)[1].lower()
    
    if extension in extensions:
      folder_name = extensions[extension]
      folder_path = os.path.join(directory, folder_name)
      os.makedirs(folder_path, exist_ok=True)
      
      destination_path = os.path.join(folder_path, folder_name)
      shutil.move(file_path, destination_path)
      
      print(f"Moved {filename} to {folder_name} folder")
    else:
      print("Cannot move file. Unknown file extension")  
  else:
    print(f"Skipped {filename}. It's a directory")
else:
  print("File organisation completed.")        
      