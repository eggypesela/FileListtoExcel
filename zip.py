import os
import shutil

def zip_folders_in_directory():
    directory_path = os.path.dirname(os.path.realpath(__file__))
    for folder in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder)
        if os.path.isdir(folder_path):
            shutil.make_archive(folder_path, 'zip', folder_path)

zip_folders_in_directory()