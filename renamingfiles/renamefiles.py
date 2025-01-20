import os
import re
import time

def rename_files_in_folder():
    print("This script was made by Igor Carvalheira. It automatically renames files in a folder.")
    print("For example, you may have files like 'GetSales2023.txt', 'GetSales2024.txt', etc.,")
    print("This script can rename them to 'Sales2023.txt', 'Sales2024.txt', etc.")
    print("Just provide the folder path, the file extension, and the pattern in the filenames.\n")

    # Get the folder path and other inputs (your original code)
    folder_path = input("Please enter the folder path: ")
    files = os.listdir(folder_path)

    print("The following files were found: ")
    for file_name in files:
        print(file_name)

    extensions = {os.path.splitext(file)[1] for file in files if os.path.isfile(os.path.join(folder_path, file))}
    extensions_string = "; ".join(sorted(extensions))
    print("The following extensions were found: " + extensions_string)

    chosen_extension = input("Please choose an extension to work with (e.g., 'mp4'): ")
    new_name_prefix = input("Please provide the new name prefix for the files: ")

    # Regular expression to find numbers, possibly with decimals
    number_pattern = r"(\d+(\.\d+)?)"  # This will match both integers and decimals like 8, 8.5, 9.7

    for file_name in files:
        if file_name.endswith("." + chosen_extension):
            # Use re.search to find the episode number
            match = re.search(number_pattern, file_name)
            
            if match:
                episode_number = match.group(1)  # This will capture the number (including decimals)
                new_name = f"{new_name_prefix} {episode_number}.{chosen_extension}"
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed: {file_name} -> {new_name}')
            else:
                print(f'Skipped: {file_name} (No episode number found)')

    print("\nProcess completed. The program will close in 11 seconds...")

    # Wait for 11 seconds before the script ends
    time.sleep(11)

if __name__ == "__main__":
    rename_files_in_folder()
