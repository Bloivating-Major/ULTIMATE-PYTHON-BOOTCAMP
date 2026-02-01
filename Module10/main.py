import shutil
from pathlib import Path

def create_folder():
    try:
        name = input("Please enter name of your folder: ")
        p = Path(name)
        p.mkdir() 
        print("Folder created successfully! ✅")
    except Exception as err:
        print(f"Sorry an error occured as {err}")
        
def read_file_folder():
    p = Path("")
    items = list(p.rglob("*"))
    if not items:
        print("📂 No files or folders found.")
        return
    for index, item in enumerate(items):
        print(f"{index+1}. {'📁' if item.is_dir() else '📄'} {item}")
    
def update_folder():
    try:
        read_file_folder()
        old_name = input("Please tell which folder you want to update: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Please tell your new folder name: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder name was updated successfully! ✅")
        else:
            print("No such folder exist!")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def delete_folder():
    try:
        read_file_folder()
        name = input("Please tell which folder you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Your folder was deleted successfully! ✅")
        else:
            print("No such folder exist!")    
    except Exception as err:
        print(f"Sorry an error occured as {err}")
        
def create_file():
    try:
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Write what you want in this file: ")
                fs.write(data)
            print("Your file was created successfully! ✅")
        else :
            print("Sorry this file name already exist!")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def read_file():
    try:
        read_file_folder()
        name = input("Please enter your file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                content = fs.read()
                print("Your file content is : ")
                print(content)
        else:
            print("Sorry no such file exist")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def update_file():
    try:
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Options : ")
            print("1. For renaming the file")
            print("2. For appending something in the file")
            print("3. For overwriting the file content")
            choice = int(input("Tell your choice: "))
            if choice == 1:
                new_name = input("Tell your new name with extension: ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name has changed successfully! ✅")
                else:
                    print(f"Sorry the file with new {new_name} already exist!")
            elif choice == 2:
                with open(p, "a") as fs:
                    data = input("What you want to append?\n")
                    fs.write(" "+data)
                print("Data appended successfully! ✅")
            elif choice == 3:
                with open(p, "w") as fs:
                    data = input("What you want to overwrite?\n")
                    fs.write(data)
                print("Data overwritten successfully! ✅") 
    except Exception as err:
        print(f"Sorry an error occured as {err}")
    
def delete_file():
    try:
        read_file_folder()
        name = input("Tell your file name with extension: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully! ✅")
        else:
            print("No such file exist!")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

while True:
    print("\n\n======================")
    print("Options : ")
    print("======================\n\n")

    print("1. Create a folder")
    print("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete the folder")
    print("5. Create a File")
    print("6. Read a File")
    print("7. Update a File")
    print("8. Delete a File")
    print("0. Exit the Program")

    try:
        choice = int(input("Please enter your option: "))

        if choice == 1:
            create_folder()
        elif choice == 2:
            read_file_folder()
        elif choice == 3:
            update_folder()
        elif choice == 4:
            delete_folder()
        elif choice == 5:
            create_file()
        elif choice == 6:
            read_file()
        elif choice == 7:
            update_file()
        elif choice == 8:
            delete_file()
        elif choice == 0:
            print("Program Exited Successfully! ✅")
            break
        else :
            print("Invalid Choice!!!\nPlease enter valid number!\nExample : 1")
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue