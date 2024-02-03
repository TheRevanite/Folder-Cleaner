import os

#Path to the folder containing the files to be deleted
folder_path='path_to_folder_to_clean'

#Path to the text file containing the list of filenames to be deleted
file_list_path='path_to_your_filenames.txt'

#Check if the folder and file list exist, and read the list of filenames from the text file
if os.path.exists(folder_path) and os.path.exists(file_list_path):
    with open(file_list_path, 'r') as file:
        filenames_to_delete=file.readlines()

    #Iterate over each filename and delete the corresponding file
    for filename in filenames_to_delete:

        #Construct the full path of the file
        file_path=os.path.join(folder_path, filename.strip())

        #Check if the file exists
        if os.path.exists(file_path):

            #Delete the file
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")

else:
    print("Folder or file list not found.")
