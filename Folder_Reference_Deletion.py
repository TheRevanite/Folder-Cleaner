import os

#Paths to the folders
folder_to_clean='path_to_folder_to_clean'
reference_folder='path_to_reference_folder'

#Get the list of files in both folders
files_to_clean=os.listdir(folder_to_clean)
reference_files=os.listdir(reference_folder)

#Convert lists to sets for efficient comparison
files_to_clean_set=set(files_to_clean)
reference_files_set=set(reference_files)

#Identify the files to delete
files_to_delete=files_to_clean_set.intersection(reference_files_set)

#Delete the files from the first folder
for file_to_delete in files_to_delete:
    file_path=os.path.join(folder_to_clean, file_to_delete)
    os.remove(file_path)
    print(f"Deleted: {file_path}")
