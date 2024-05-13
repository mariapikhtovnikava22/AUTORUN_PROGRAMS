import os
from tkinter import messagebox
from checks.checks import show_error_message
import re

def get_autostart_programs():
    autostart_directory = os.path.expanduser('~/.config/autostart/')
    autostart_programs = []

    if os.path.exists(autostart_directory) and os.path.isdir(autostart_directory):
        for filename in os.listdir(autostart_directory):
            file_path = os.path.join(autostart_directory, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    for line in file:
                        if line.startswith("Name="):
                            program_name = line.strip().split("=")[1]
                            autostart_programs.append(program_name)

    return autostart_programs


def find_program_by_name(program_name):
    autostart_directory = os.path.expanduser('~/.config/autostart/')
    matching_files = []

    if os.path.exists(autostart_directory) and os.path.isdir(autostart_directory):
        for filename in os.listdir(autostart_directory):
            file_path = os.path.join(autostart_directory, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    for line in file:
                        if program_name in line:
                            matching_files.append(filename)
                            break  # Найдено соответствие, прерываем цикл чтения файла

    return matching_files


def get_name_and_path(filepath):
    content = None
    name = ""
    path = ""

    with open(filepath, 'r') as o_file:
        content = o_file.read()

    name_match = re.search(r'Name\s*=\s*(.*)', content)
    path_match = re.search(r'Exec\s*=\s*(.*)', content)

    if name_match:
        name += name_match.group(1)
    if path_match:
        path += path_match.group(1)

    return name, path


def get_program_name(program_path):
    return program_path.split("/")[-1]


class GenerateDesktopFile:
    def __init__(self, name, path):
        self.directory = "/home/maria/.config/autostart"
        self.program_path = path
        self.program_name = get_program_name(self.program_path)
        self.autostart_name = name
        self.create_desktop_file()

    def create_desktop_file(self):
        if self.program_path and self.program_name and self.autostart_name:
            desktop_filename = f"{self.directory}/{self.program_name}.desktop"
            desktop_content = f"""[Desktop Entry]
Type=Application
Exec={self.program_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name={self.autostart_name}
Comment=
        """
            with open(desktop_filename, 'w') as desktop_file:
                desktop_file.write(desktop_content)

    def delete_desktop_file(self, program_name, parent):
        program_name_in_directory = find_program_by_name(program_name)[0]
        file_path = os.path.join(self.directory, program_name_in_directory)
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Inforamtion", f"The {file_path} file has been successfully deleted.", parent=parent)
        else:
            show_error_message(f"There is no file with this path {file_path}", parent)
