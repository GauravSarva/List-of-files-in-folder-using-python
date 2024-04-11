import os

folders = input("Please provide list of folder names with spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("\n Please provide a valid folder name, looks like the folder does not exist:" + folder)
        continue
    except PermissionError:
        print("\n No access to this folder: " + folder)
        continue

    print("\n === Listing files for the folder - " + folder)
    
    for file in files:
        print(file)