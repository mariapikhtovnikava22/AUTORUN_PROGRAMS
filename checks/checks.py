import os
from tkinter import messagebox
from checks.check_errors import check_file_exists, check_file_permissions


def show_error_message(message, parent):
    messagebox.showerror("Error", message, parent=parent)


def check_add(name, file_path, parent):
    if not name:
        show_error_message("The field and the program name should not be empty", parent)
        return False
    if not file_path:
        show_error_message("Specify the path to the file", parent)
        return False
    if not (check_file_exists(name, file_path)):
        show_error_message("A program with the same name or path already exists", parent)
        return False
    if not (os.path.exists(file_path)):
        show_error_message("There is no file with this path", parent)
        return False
    if not (check_file_permissions(file_path)):
        show_error_message("Not an executable file or a file that runs on behalf of the administrator", parent)
        return False

    return True