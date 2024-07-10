import os

def find_zip_files(folder_path):
    zip_files = []
    try:
        # Get all items (files and folders) in the current folder
        items = os.listdir(folder_path)
        # Iterate through each item
        for item in items:
            # E.g item would be example.zip
            item_path = os.path.join(folder_path, item)
            # item_path would be /home/user/Documents/example1.zip

            # Check if the item is a file with a .zip extension
            if os.path.isfile(item_path) and item.endswith('.zip'):
                # The following would look like: ('/home/user/Documents/example1.zip', '/home/user/Documents')
                zip_files.append((item_path, os.path.dirname(item_path)))

            # Check if the item is a directory
            elif os.path.isdir(item_path):
                # Recursively search for zip files
                # list .extend in python - adding the recursively returned zip files to list
                zip_files.extend(find_zip_files(item_path))
    except OSError as e:
        print(f"Error accessing folder {folder_path}: {e}")
    return zip_files
    

def find_and_print_zip_files(root_directory):
    """If Zip files are found then print them"""
    zip_files_found = find_zip_files(root_directory)
    if zip_files_found:
        # IF zip files are found print through the list of tuples
        for i, (zip_file, top_level_dir) in enumerate(zip_files):
            print(f"Zip file {i + 1}: {zip_file}")

# Example usage:
if __name__ == "__main__":
    root_directory = r'C:\Users\susan\Desktop\Michael\Client O-P'
    find_and_print_zip_files(root_directory)