import os

DOWNLOADS_PATH = os.path.expanduser('~') + os.sep + 'Downloads' 
ORGANIZED_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.ico'],
    'Audio': ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac'],
    'Video': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.bz2'],
    'Executables': ['.exe', '.bat', '.sh', '.msi'],
    'Others': []
}

def get_folder(filename, organized_folders):
    # print(os.path.splitext(filename))
    file_type = os.path.splitext(filename)[1]
    for folder, extensions in organized_folders.items():
        if file_type in extensions:
            return folder
    return 'Others'

def organize(organized_folders):
    for filename in os.listdir(DOWNLOADS_PATH):
        # print(filename)
        if os.path.isfile(os.path.join(DOWNLOADS_PATH, filename)):
            folder = get_folder(filename, organized_folders)
            folder_path = os.path.join(DOWNLOADS_PATH, folder)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            os.rename(os.path.join(DOWNLOADS_PATH, filename), os.path.join(folder_path, filename))

if __name__ == '__main__':
    organize(ORGANIZED_FOLDERS)
    print("Downloads organized!")