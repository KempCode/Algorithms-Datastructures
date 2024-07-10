import os

def find_zip_files(folder_path):
    zip_files = []

    try:
        # Get all items (files and folders) in the current folder
        items = os.listdir(folder_path)

        # Iterate through each item
        for item in items:
            item_path = os.path.join(folder_path, item)

            # Check if the item is a file with a .zip extension
            if os.path.isfile(item_path) and item.endswith('.zip'):
                zip_files.append((item_path, os.path.dirname(item_path)))

            # Check if the item is a directory
            elif os.path.isdir(item_path):
                # Recursively search for zip files
                zip_files.extend(find_zip_files(item_path))

    except OSError as e:
        print(f"Error accessing folder {folder_path}: {e}")

    return zip_files

def print_zip_file_info(zip_files):
    for i, (zip_file, top_level_dir) in enumerate(zip_files):
        print(f"Zip file {i + 1}: {zip_file}")

def find_and_print_zip_files(root_directory):
    zip_files_found = find_zip_files(root_directory)
    if zip_files_found:
        print_zip_file_info(zip_files_found)

# Example usage:
if __name__ == "__main__":
    root_directory = r'C:\Users\susan\Desktop\Michael\Client O-P'
    find_and_print_zip_files(root_directory)