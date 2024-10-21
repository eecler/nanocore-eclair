import random
import os
from FileSystem import fcreate, fdelete, md, rd, edit_file, ls, lsl, lsa, lslh, cd, hide_folder, unhide_folder

def help_menu():
    print("""
Help menu:
help - this menu
random - generating random number
shutdown - shutdown os
touch <filename> - create a new file
edit <filename> - edit an existing file
delete - delete a file or folder
md <foldername> - create a new directory
rd <foldername> - remove a directory and its contents
ls - list all files and directories
lsl - list all files and directories with details
lsa - list all files and directories including hidden
lslh - list all files and directories with details and sizes
cd <foldername> - change directory
hide <foldername> - hide a folder
unhide <foldername> - unhide a folder
""")


def parse_command(user_input):
    words = user_input.split()
    if words:
        command = words[0]
        args = ' '.join(words[1:])
        return command, args
    return None, None
    
def command_list(user_input):
    user_input = input(">")
    command, args = parse_command(user_input)
    if command == "help":
        help_menu()
    elif command == "random":
        import random
        random_int = random.randint(0, 327679736)
        print(random_int)
    elif command == "shutdown":
        exit()
    elif command == "touch":
        filename = args.strip()
        fcreate(filename)
    elif command == "edit":
        filename = args.strip()
        edit_file(filename)
    elif command == "delete":
        filename = args.strip()
        if not filename:
            print("Specify the filename after 'delete'")
        else:
            fdelete(filename)
    elif command == "md":
        folder_name = args.strip()
        md(folder_name)
    elif command == "rd":
        folder_name = args.strip()
        rd(folder_name)
    elif command == "ls":
        ls()
    elif command == "lsl":
        lsl()
    elif command == "lsa":
        lsa()
    elif command == "lslh":
        lslh()
    elif command == "cd":
        folder_name = args.strip()
        cd(folder_name)
    elif command == "hide":
        folder_name = args.strip()
        hide_folder(folder_name)
    elif command == "unhide":
        folder_name = args.strip()
        unhide_folder(folder_name)
    else:
        print("Unknown command. Type 'help' for a list of commands.")

