# File Cleaner

Don't you just HATE it when you have to delete certain files, but there's thousands of files that you have to sift through? Or even worse, you KNOW what files you have to delete; maybe you have the file names in a notepad. Or, even worse, you have the exact same files in another folder, thinking that there must be some way to use that folder as a reference...
Well here are two simple python programs created for that very purpose!

## Features

- **[Folder_Reference_Deletion](https://github.com/TheRevanite/Folder-Cleaner/blob/main/Folder_Reference_Deletion.py)**: Delete specific files, editing two lines: the path to your reference folder, and the path to your actual folder (where you wanna delete stuff).
- **[File_Reference_Deletion](https://github.com/TheRevanite/Folder-Cleaner/blob/main/File_Reference_Deletion.py)**: Delete specific files, editing two lines: the path to your reference filename (eg. references.txt), and the path to your actual folder (where you wanna delete stuff).

## Usage

1. **Ensure Correct File Paths**:
   - Double-check that the paths to your folder and the text file containing the list of filenames are correct. Provide the full paths like `/path/to/folder_to_clean`, `/path/to/folder_reference`, and `/path/to/your/filenames.txt`.

2. **File List Formatting**:
   - Make sure the text file containing the list of filenames has one filename per line. Avoid extra spaces or characters that might cause parsing issues.

3. **Permissions**:
   - Ensure that the Python script has the necessary permissions to read from the text file and delete files in the specified folder.

## Contributors

- [Megh Mavani](https://github.com/TheRevanite/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest improvements to enhance the functionality of this file cleaner tool!
