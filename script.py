
files_edited = []

import os
import shutil

# Define the subfolder path from which you want to copy files
subfolder_path = "/subs"  # Update this with the path to your subfolder

# Loop through the files in the current directory
current_folder = os.getcwd()  # Gets the current directory

for filename in os.listdir(current_folder):
    # Skip if it's a directory or if it's the script itself
    if os.path.isdir(filename) or filename == os.path.basename(__file__):
        continue
    
    # Copy a file from the subfolder
    source_file = os.path.join(subfolder_path, "file_to_copy.ext")  # Replace with your specific file
    if not os.path.exists(source_file):
        print(f"Source file {source_file} does not exist.")
        continue
    
    # Generate the new file name by appending something to the original name
    new_filename = f"copy_of_{filename}"  # Modify this to suit your renaming needs
    
    # Define the destination path in the current folder
    destination_file = os.path.join(current_folder, new_filename)
    
    # Copy the file from the subfolder and rename it
    shutil.copy(source_file, destination_file)
    print(f"Copied and renamed {source_file} to {destination_file}")

print("Done.")