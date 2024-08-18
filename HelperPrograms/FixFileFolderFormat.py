import os
import re
import pandas as pd
import subprocess
import shutil

def extract_client_number(client_info):
    # Find the last occurrence of " - "
    last_dash_index = client_info.rfind(" - ")

    if last_dash_index != -1:
        # Extract the client number from the substring after the last " - "
        client_number = client_info[last_dash_index + 3:]  # Skip over " - "
        return client_number.strip()
    else:
        print("Cant extract client number")
        return client_info


def move_and_rename_folder(source_folder, destination_parent, new_name):
    try:
        # Create the destination directory if it doesn't exist
        os.makedirs(destination_parent, exist_ok=True)
        
        # Construct the destination path with the new name
        destination_folder = os.path.join(destination_parent, new_name)
        
        # Move the source folder to the destination with shutil.move
        shutil.move(source_folder, destination_folder)
    
    except FileNotFoundError:
        print(f"Error: Source directory '{source_folder}' not found.")
    except PermissionError:
        print(f"Error: Permission denied moving '{source_folder}' to '{destination_parent}'.")
    except shutil.Error as e:
        print(f"Error: {e}")



def check_clients_and_matters(root_dir, excel_filename):
    """Main function to check if clients and matters fit prescribed format"""
    client_pattern = r'^.*\s-\s[A-Za-z0-9]{3}[0-9]{4,5}$'
    matter_pattern = r'^\d{3}\s?- .+|\d{3}\s.+$'

    # Get the list of Client directories.
    subdirs = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]


    # Check each Client Directory.
    for client in subdirs:
        client_path = os.path.join(root_dir, client)
        matters = [name for name in os.listdir(client_path) if os.path.isdir(os.path.join(client_path, name))] #Get matter names
       

        # if Client directory doesnt follow pattern dont bother checking the matters. Move to BrokenClients Dir.
        if not re.match(client_pattern, client):
            print('Client Directory doesnt follow format')
            move_and_rename_folder(client_path, r'C:\Users\susan\Desktop\Michael\BrokenClients', client)
            continue

     
        # Check each Matter Directory under the current Client.
        for matter in matters:
            matter_path = os.path.join(client_path, matter)
            matter_valid = re.match(matter_pattern, matter)
            
            # Check if the matter directory follows the pattern
            if not matter_valid:
                print("Matter not valid in: ", client)
                print("The matter is : ", matter)
                # Now if theres an invalid matter in a valid client - want to leave the client but
                # move BON41594. invalid matter name ... to matter errors dir.
                move_and_rename_folder(matter_path, r'C:\Users\susan\Desktop\Michael\BrokenMatters', f"{extract_client_number(client)}.{matter}")
            else:
                # If matter follows pattern
                move_and_rename_folder(matter_path, r'C:\Users\susan\Desktop\Michael\Matters', f"{extract_client_number(client)}.{matter[:3]}")
                print(f"{extract_client_number(client)}.{matter[:3]}")

            
        if re.match(client_pattern, client):
            # Client does follow format
            # After matters are moved move the client to correct dir.
            # if directory is not empty then (Only want clients with clientdocs):
            # Can easily remove this line if LEAP need ALL client folders even empty ones.
            if os.listdir(client_path):
                move_and_rename_folder(client_path, r'C:\Users\susan\Desktop\Michael\Clients', extract_client_number(client))
                print("EXTRACTING CLIENT NUMBER: ")
                print(extract_client_number(client))
           

       

root_directory = r'C:\Users\susan\Desktop\Michael\Client Patel'
excel_file = r'C:\Users\susan\Desktop\Michael\Errors.xlsx'
check_clients_and_matters(root_directory, excel_file)

