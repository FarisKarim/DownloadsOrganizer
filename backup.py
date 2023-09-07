import os
import shutil

DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
BACKUP_PATH = os.path.join(os.path.expanduser('~'), 'Downloads_backup')

def backup_downloads():
    if not os.path.exists(BACKUP_PATH):
        shutil.copytree(DOWNLOADS_PATH, BACKUP_PATH)
        print(f"Backup completed to: {BACKUP_PATH}")
    else:
        print(f"Backup directory {BACKUP_PATH} already exists.")

if __name__ == "__main__":
    backup_downloads()
