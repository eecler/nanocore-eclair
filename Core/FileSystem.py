import os
import shutil

protected_folders = ["Core", "NanoCore", ".git"]
protected_files = ["FileSystem.py", "README.md", "main.py", "Commands.py", "LICENSE", ".gitignore.txt"]


def fcreate(filename):
    if not filename:
        print("Specify the filename after 'touch'")
        return

    if not os.path.exists(filename):
        with open(filename, "w+") as file:
            print(f"File '{filename}' created")
    else:
        print(f"File '{filename}' already exists")


def fdelete(filename):
    if not filename:
        print("Specify the filename after 'delete'")
        return

    if filename in protected_files or filename in protected_folders:
        print(f"'{filename}' is protected and cannot be deleted.")
        return

    if os.path.exists(filename):
        try:
            if os.path.isdir(filename):
                shutil.rmtree(filename)
                print(f"Folder '{filename}' deleted along with its contents")
            else:
                os.remove(filename)
                print(f"File '{filename}' deleted")
        except PermissionError:
            print(f"Permission denied: cannot delete '{filename}'. Check your permissions.")
        except Exception as e:
            print(f"Error when deleting '{filename}': {e}")
    else:
        print(f"File or folder '{filename}' does not exist")


def md(folder_name):
    if folder_name:
        try:
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created.")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")
        except Exception as e:
            print(f"Error when creating a folder: {e}")
    else:
        print("Specify the folder name after 'md'")


def rd(folder_name):
    if folder_name in protected_folders:
        print(f"Folder '{folder_name}' is protected and cannot be deleted.")
        return

    if folder_name:
        try:
            shutil.rmtree(folder_name)
            print(f"Folder '{folder_name}' and its contents deleted.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' does not exist.")
        except PermissionError:
            print(f"Permission denied: cannot delete '{folder_name}'. Check your permissions.")
        except Exception as e:
            print(f"Error when deleting the folder: {e}")
    else:
        print("Specify the folder name after 'rd'")


def edit_file(filename):
    if not filename:
        print("Specify the filename after 'edit'")
        return

    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist. Creating a new file.")
        with open(filename, "w+") as file:
            pass

    with open(filename, "r+") as file:
        content = file.readlines()

        print(f"Editing file: {filename}")
        for i, line in enumerate(content):
            print(f"{i + 1:4}: {line}", end="")

        print(
            "\nEnter new content line by line. Type 'SAVE' to save and exit, 'EXIT' to exit without saving, or 'EDIT <line_number>' to edit a specific line.")
        new_content = content.copy()
        while True:
            line = input("> ")
            if line.strip().upper() == "SAVE":
                break
            elif line.strip().upper() == "EXIT":
                print("Exiting without saving.")
                return
            elif line.strip().upper().startswith("EDIT"):
                try:
                    line_number = int(line.strip().split()[1])
                    if 1 <= line_number <= len(new_content):
                        print(f"Current line {line_number}: {new_content[line_number - 1]}")
                        new_text = input("Enter new text: ")
                        new_content[line_number - 1] = new_text + "\n"
                    else:
                        print(f"Line number {line_number} is out of range.")
                except (IndexError, ValueError):
                    print("Invalid line number. Use 'EDIT <line_number>'.")
            else:
                new_content.append(line + "\n")

        file.seek(0)
        file.writelines(new_content)
        file.truncate()
        print(f"File '{filename}' updated.")


def ls():
    print("\n".join(os.listdir(".")))


def lsl():
    for item in os.listdir("."):
        fullpath = os.path.join(".", item)
        try:
            print(f"{'d' if os.path.isdir(fullpath) else '-'} "
                  f"{'r' if os.access(fullpath, os.R_OK) else '-'}"
                  f"{'w' if os.access(fullpath, os.W_OK) else '-'} "
                  f"{'x' if os.access(fullpath, os.X_OK) else '-'} {item}")
        except Exception as e:
            print(f"Error accessing '{item}': {e}")


def lsa():
    print("\n".join(os.listdir(".")))


def lslh():
    for item in os.listdir("."):
        fullpath = os.path.join(".", item)
        try:
            size = os.path.getsize(fullpath)
            print(
                f"{size} {'d' if os.path.isdir(fullpath) else '-'} "
                f"{'r' if os.access(fullpath, os.R_OK) else '-'}"
                f"{'w' if os.access(fullpath, os.W_OK) else '-'} "
                f"{'x' if os.access(fullpath, os.X_OK) else '-'} {item}"
            )
        except Exception as e:
            print(f"Error accessing '{item}': {e}")

def cd(folder_name=""):
    if not folder_name:
        print(f"Current directory: {os.getcwd()}")
        return

    if folder_name == "..":
        try:
            os.chdir("..")
            print(f"Changed directory to '{os.getcwd()}'")
        except Exception as e:
            print(f"Error when changing directory: {e}")
    else:
        try:
            os.chdir(folder_name)
            print(f"Changed directory to '{folder_name}'")
            print(f"Current directory: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' does not exist.")
        except NotADirectoryError:
            print(f"'{folder_name}' is not a directory.")
        except Exception as e:
            print(f"Error when changing directory: {e}")

def hide_folder(folder_name):
    if os.path.exists(folder_name):
        try:
            os.system(f'attrib +h {folder_name}')
            print(f"Folder '{folder_name}' is now hidden.")
        except Exception as e:
            print(f"Error when hiding the folder: {e}")
    else:
        print(f"Folder '{folder_name}' does not exist.")

def unhide_folder(folder_name):
    if os.path.exists(folder_name):
        try:
            os.system(f'attrib -h {folder_name}')
            print(f"Folder '{folder_name}' is now visible.")
        except Exception as e:
            print(f"Error when unhiding the folder: {e}")
    else:
        print(f"Folder '{folder_name}' does not exist.")
