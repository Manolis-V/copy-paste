import os
import shutil

# Loop through the files in the current directory
current_folder = os.getcwd()  # Gets the current directory
srt_file_to_copy = "2_English.srt"
for filename in os.listdir(current_folder):
    # Skip if it's a directory or if it's the script itself
    if os.path.isdir(filename) or filename == os.path.basename(__file__):
        continue

    filename = filename.split(".mp4")[0]
    print("# "+ current_folder)
    # Define the subfolder path from which you want to copy files
    subfolder_path = current_folder + "\Subs\\" + filename 

    # Copy a file from the subfolder
    source_file = os.path.join(subfolder_path, srt_file_to_copy)
    if not os.path.exists(source_file):
        print(f"Source file {source_file} does not exist.")
        continue
    
    # Generate the new file name by appending something to the original name
    new_filename = filename + ".srt"
    
    # Define the destination path in the current folder
    destination_file = os.path.join(current_folder, new_filename)
    
    # Copy the file from the subfolder and rename it
    shutil.copy(source_file, destination_file)
    print(f"Copied and renamed {source_file} to {destination_file}")

print("Done.")