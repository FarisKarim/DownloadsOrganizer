import os
import shutil
import json

DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
BACKUP_PATH = os.path.join(os.path.expanduser('~'), 'Downloads_backup')
MOVES_FILE = 'moves_made.json'

ORGANIZED_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.ico'],
    'Audio': ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac'],
    'Video': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.bz2'],
    'Executables': ['.exe', '.bat', '.sh', '.msi'],
    'Others': []
}

def backup_downloads():
    if not os.path.exists(BACKUP_PATH):
        shutil.copytree(DOWNLOADS_PATH, BACKUP_PATH)
        print(f"Backup completed to: {BACKUP_PATH}")
    else:
        print(f"Backup directory {BACKUP_PATH} already exists. Consider renaming or deleting it before creating a new backup.")

def move_file(filename, folder_name):
    folder_path = os.path.join(DOWNLOADS_PATH, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    original_location = os.path.join(DOWNLOADS_PATH, filename)
    new_location = os.path.join(folder_path, filename)

    shutil.move(original_location, new_location)
    return original_location, new_location

def organize_downloads():
    backup_choice = input("Would you like to backup your Downloads folder before organizing? (y/n): ").lower()
    if backup_choice == 'y':
        backup_downloads()

    moves_made = []
    for filename in os.listdir(DOWNLOADS_PATH):
        if os.path.isfile(os.path.join(DOWNLOADS_PATH, filename)):
            file_ext = os.path.splitext(filename)[1]

            folder_name = 'Others'  # Default value
            for folder, extensions in ORGANIZED_FOLDERS.items():
                if file_ext in extensions:
                    folder_name = folder
                    break

            moves_made.append(move_file(filename, folder_name))
    
    with open(MOVES_FILE, 'w') as f:
        json.dump(moves_made, f)
    print("Downloads folder organized successfully!")

def undo_last_moves():
    try:
        with open(MOVES_FILE, 'r') as f:
            moves = json.load(f)

        for original_location, new_location in moves:
            if os.path.exists(new_location):
                shutil.move(new_location, original_location)
        os.remove(MOVES_FILE)
        print('Last moves undone successfully!')
    except FileNotFoundError:
        print("No moves to undo!")

if __name__ == "__main__":
    action = input("Do you want to organize or undo? (Type 'organize' or 'undo'): ").lower()
    actions = {'organize': organize_downloads, 'undo': undo_last_moves}
    actions.get(action, lambda: print("Invalid choice!"))()




