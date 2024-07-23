import os
import re

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
    

def is_duplicate_client(root_dir):
    """Function to check for duplicate client directories within the root directory"""
    # Get the list of Client directories.
    clients = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]
    client_pattern = r'^.*\s-\s[A-Za-z0-9]{3}[0-9]{4,5}$'

    
    seen_clients = set()

    # Check each Client Directory.
    for client in clients:
        if re.match(client_pattern, client):
            if extract_client_number(client) in seen_clients:
                print(f'Duplicate client directory found: {client}')
            else:
                seen_clients.add(extract_client_number(client))

# Example usage
root_directory = r'C:\Users\susan\Desktop\Michael\Client A-B'
is_duplicate_client(root_directory)