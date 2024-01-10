import os
import pandas as pd
from datetime import datetime

# Define the directory path
#dir_path = os.path.dirname(os.path.realpath(__file__))

# Ask the user the directory path
dir_path = input("Please input directory path : ")

# Create an empty list to store file properties
file_properties = []

# Loop through each file in the directory
for root, dirs, files in os.walk(dir_path):
    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(root, file_name)
        # Get the folder path of the file
        folder_path = os.path.join(root)
        # Get the file size in bytes
        file_size = ((os.path.getsize(file_path))/1024)
        # Get the file creation time
        file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        # Get the file last access time
        file_atime = datetime.fromtimestamp(os.path.getatime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        # Get the file last modify time
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        # Add the file name and properties to the list
        file_properties.append([folder_path, file_name, file_size, file_ctime, file_atime, file_mtime])

# Convert the list to a pandas DataFrame
df = pd.DataFrame(file_properties, columns=['File Directory', 'File Name', 'File Size (kilobytes)', 'Creation Time', 'Last Access Time', 'Last Modify Time'])

# Create path variable to output file
excel_location = dir_path + "\\""" +'File List.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_location, index=False)