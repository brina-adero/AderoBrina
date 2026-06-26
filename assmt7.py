import os
import shutil

# Define the path to the Downloads folder
# NOTE: Change "YourUsername" to your actual Windows username
DOWNLOADS_DIR = "C:/Users/YourUsername/Downloads"

# Dictionary to map file extensions to target folder names
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg"]
}

def organize_downloads():
    print("STARTING FILE ORGANIZATION")
    
    # Check if the path actually exists before running
    if not os.path.exists(DOWNLOADS_DIR):
        print(f"Error: The directory {DOWNLOADS_DIR} does not exist.")
        return

    # Change the current working directory to Downloads
    os.chdir(DOWNLOADS_DIR)
    
    # Loop through all files in the directory
    for item in os.listdir():
        # Skip if it is a directory 
        if os.path.isdir(item):
            continue
            
        # Get the file extension and make it lowercase
        filename, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()
        
        # Track if we found a match for the file type
        moved = False
        
        # Check which folder the file belongs to
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                # Create the folder if it doesn't exist yet
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    print(f"Created new folder: {folder_name}")
                
                # Move the file into the folder
                shutil.move(item, os.path.join(folder_name, item))
                print(f"Moved: {item} -> {folder_name}/")
                moved = True
                break
                
        # If the file extension isn't in our list, put it in an 'Others' folder
        if not moved:
            other_folder = "Others"
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(item, os.path.join(other_folder, item))
            print(f"Moved: {item} -> {other_folder}/")

    print("--- ORGANIZATION COMPLETE ---")

# Run the program
if __name__ == "__main__":
    organize_downloads()
