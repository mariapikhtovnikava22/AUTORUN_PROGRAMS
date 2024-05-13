import os
import re


def check_file_exists(name, path):
    directory = '/home/maria/.config/autostart'

    files = os.listdir(directory)

    for file in files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r') as o_file:
            content = o_file.read()
            # Проверка наличия целевых полей в содержимом файла с использованием регулярных выражений
            if re.search(fr"^{re.escape(name)}\s*=", content, re.MULTILINE) and re.search(fr"^{re.escape(path)}\s*=", content, re.MULTILINE):
                return False
    return True


def check_file_permissions(file_path):
    return os.access(file_path, os.X_OK)


