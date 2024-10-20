# Script for Copying and Renaming `.srt` Files for `.mp4` Videos

This Python script copies a `.srt` file (specifically `2_English.srt`) from a designated subfolder and renames it to match each `.mp4` file found in the current directory. The `.srt` file is placed alongside the corresponding `.mp4` file, allowing for easy subtitle usage.

## Requirements

- Python 3.x
- A folder containing `.mp4` files
- A subfolder containing the `.srt` file to copy (named `2_English.srt`)

## How It Works

- The script looks for all `.mp4` files in the current directory (the directory where the script is located).
- For each `.mp4` file, the script:
    1. Copies the `2_English.srt` file from a designated subfolder.
    2. Renames the copied `.srt` file to match the `.mp4` file (but keeps the `.srt` extension).

For example:
- If you have a file `movie.mp4`, the script will create a copy of `2_English.srt` named `movie.srt` in the same directory as `movie.mp4`.

## Installation
1. Clone or download this script.
2. Place the script in the same folder as the `.mp4` files you want to process.
3. Ensure the `2_English.srt` file is placed in the specified subfolder.

## Usage
1. Open a terminal or command prompt.

2. Navigate to the folder where your .mp4 files and this script are located.

3. Run the script using the following command:

```bash
python3 script.py
```
4. The script will process all `.mp4` files in the current directory, copying and renaming the `2_English.srt` file accordingly.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder where your `.mp4` files and this script are located.
3. Run the script using the following command:

   ```bash
   python3 script.py
   ```

## Example
- Suppose you have the following files in your directory:
```bash
movie1.mp4
movie2.mp4
movie3.mp4
```
    - And you have the `2_English.srt` file located in a subfolder.
- After running the script, you will get:
```bash
movie1.mp4
movie1.srt
movie2.mp4
movie2.srt
movie3.mp4
movie3.srt
```

## Customization
- To change the subfolder where the `2_English.srt` file is located, edit the subfolder_path variable in the script.
- If you want to copy a different `.srt` file, modify the `srt_file_to_copy` variable in the script.

## Troubleshooting
- File Not Found Error: Ensure that the `2_English.srt` file exists in the correct subfolder.
- Script Doesn't Find `.mp4` Files: Ensure you're running the script from the directory where your `.mp4` files are located.