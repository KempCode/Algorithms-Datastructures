import os
import time

def remove_empty_folders(directory):
    # Traverse the directory tree from bottom to top
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            try:
                # Check if the folder is empty
                if not os.listdir(folder_path):
                    # Attempt to remove the directory
                    os.rmdir(folder_path)
                    print(f"Removed empty folder: {folder_path}")
                else:
                    print(f"Skipped non-empty folder: {folder_path}")
            except OSError as e:
                # Handle any errors that occur during removal (e.g., permissions)
                print(f"Failed to remove folder: {folder_path}. Error: {e}")
                # You can implement retry logic here if needed
                # Example: wait for a short time and retry
                time.sleep(0.1)  # Wait for 0.1 seconds and retry
                try:
                    os.rmdir(folder_path)
                    print(f"Retried and removed empty folder: {folder_path}")
                except OSError as e:
                    print(f"Final attempt failed to remove folder: {folder_path}. Error: {e}")

# Example usage:
directory_to_clean = r'C:\Users\susan\Desktop\Michael\Clients'
remove_empty_folders(directory_to_clean)