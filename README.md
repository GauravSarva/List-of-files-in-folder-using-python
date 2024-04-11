# List-of-files-in-folder-using-python

This code defines a simple Python script that lists the files in a set of folders provided by the user.
The user is prompted to enter a list of folder names separated by spaces, and the script uses the os.listdir() function to list the files in each folder.
The script handles FileNotFoundError and PermissionError exceptions that might occur when trying to access the folders, and prints out an error message for each invalid folder.
The script uses a for loop to iterate through the list of folder names and prints out the list of files for each valid folder.
The script is useful for quickly checking the contents of multiple folders without having to navigate to each one individually.
