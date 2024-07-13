import os
import platform
import time

def set_file_modification_date(file_path, modification_date):
    if platform.system() == 'Windows':
        # Windows specific way to set modification time
        # Convert date to Windows format
        modification_time = time.mktime(time.strptime(modification_date, "%d.%m.%y"))
        os.utime(file_path, (modification_time, modification_time))
    else:
        # Unix/Linux specific way to set modification time
        # Convert date to Unix timestamp
        modification_time = time.mktime(time.strptime(modification_date, "%d.%m.%y"))
        os.utime(file_path, (modification_time, modification_time))

def main():
    file_name = "MyTextFile.txt"
    file_content = "This is the text file content\n"
    modification_date = "01.01.22"

    # Create the text file and write content
    with open(file_name, 'w') as file:
        file.write(file_content)

    # Set the modification date of the file
    set_file_modification_date(file_name, modification_date)

    print(f"File '{file_name}' created with modification date set to {modification_date}")

if __name__ == "__main__":
    main()