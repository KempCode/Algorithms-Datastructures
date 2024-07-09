import os
import datetime

def update_folder_date(folder_path):
    try:
        # Get all items (files and folders) in the current folder
        items = os.listdir(folder_path)

        if not items:
            print(f"Skipping empty directory: {folder_path}")
            return

        newest_timestamp = datetime.datetime.fromtimestamp(0)  # Initialize with a very old date

        # Iterate through each item
        for item in items:
            item_path = os.path.join(folder_path, item)

            # Check if the item is a file
            if os.path.isfile(item_path):
                # Get the modification timestamp of the file
                file_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
                # Update newest_timestamp if the current file is newer
                if file_timestamp > newest_timestamp:
                    newest_timestamp = file_timestamp

            # Check if the item is a directory
            elif os.path.isdir(item_path):
                # Recursively update the folder's timestamp
                update_folder_date(item_path)
                # Get the modification timestamp of the directory
                dir_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
                # Update newest_timestamp if the current directory is newer
                if dir_timestamp > newest_timestamp:
                    newest_timestamp = dir_timestamp

        # Update the folder's modification timestamp to the newest found timestamp
        os.utime(folder_path, (os.path.getatime(folder_path), newest_timestamp.timestamp()))
        print(f"Updated timestamp of folder: {folder_path} to {newest_timestamp.timestamp()}")
    
    except OSError as e:
        print(f"Error updating timestamp for folder {folder_path}: {e}")

# Example usage:
root_directory = r'C:\Users\susan\Desktop\Michael\Client A-B'
update_folder_date(root_directory)