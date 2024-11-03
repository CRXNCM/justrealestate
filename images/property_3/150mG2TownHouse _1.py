import os

def rename_files(directory, common_name):
    # Change to the target directory
    os.chdir(directory)
    
    # Loop through all files in the directory
    for i, filename in enumerate(os.listdir(directory), start=1):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        
        # Create new filename with the provided common name and number
        new_name = f"{common_name}_{i}{file_ext}"
        
        # Rename the file
        os.rename(filename, new_name)
        print(f"Renamed '{filename}' to '{new_name}'")

# User inputs for directory and common name
directory = input("Enter the directory path: ")
common_name = input("Enter the common name for the files: ")

# Call the function
rename_files(directory, common_name)
