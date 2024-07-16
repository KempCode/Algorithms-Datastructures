import os
import re
import pandas as pd

def subdirectory_exists(parent_dir):
    """Check if subdirectories exist and return boolean"""
    items = os.listdir(parent_dir)
    for item in items:
        item_path = os.path.join(parent_dir, item)
        if os.path.isdir(item_path):
            return True
    return False

def export_to_excel(data, excel_filename):
    """Exports data to excel"""
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data, columns=['Client Name', 'Reason', 'Reason1', 'Reason2', 'Reason3'])
    # Write DataFrame to Excel file
    if os.path.isfile(excel_filename):
        with pd.ExcelWriter(excel_filename, mode='a') as writer:
            # Write DataFrame to the specified sheet without index
            df.to_excel(writer, sheet_name='Non-conforming Directories', index=False)
    else:
        print("Excel Sheet doesn't exist")

def check_clients_and_matters(root_dir, excel_filename):
    """Main function to check if clients and matters fit prescribed format"""
    client_pattern = r'^.*\s-\s[A-Za-z0-9]{3}[0-9]{4,5}$'
    matter_pattern = r'^\d{3}\s?- .+|\d{3}\s.+$'

    subdirs = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]
    data = []

    for client in subdirs:
        client_path = os.path.join(root_dir, client)
        matters = [name for name in os.listdir(client_path) if os.path.isdir(os.path.join(client_path, name))]

        # Initialize reasons
        reason = ''
        reason1 = ''
        reason2 = ''
        reason3 = ''  # Initialize outside the loop

        files_in_client = [file for file in os.listdir(client_path) if os.path.isfile(os.path.join(client_path, file))]
        if files_in_client and not subdirectory_exists(client_path):
            reason3 = "Files in Client no Matters exist"

        for matter in matters:
            matter_path = os.path.join(client_path, matter)
            matter_valid = re.match(matter_pattern, matter)

            if not matter_valid:
                reason1 = 'Matter Directory doesnt follow format'
            
            if subdirectory_exists(matter_path):
                reason2 = 'Check the subdirectories in the matter'
        
        if not re.match(client_pattern, client):
            reason = 'Client Directory doesnt follow format'

        # Append to data if any reason is present
        if reason or reason1 or reason2 or reason3:
            data.append({'Client Name': client, 'Reason': reason, 'Reason1': reason1, 'Reason2': reason2, 'Reason3': reason3})

    export_to_excel(data, excel_filename)

root_directory = r'C:\Users\susan\Desktop\Michael\Client A-B'
excel_file = r'C:\Users\susan\Desktop\Michael\Errors.xlsx'
check_clients_and_matters(root_directory, excel_file)