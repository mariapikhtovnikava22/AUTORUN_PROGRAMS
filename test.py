import os


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


# Пример использования
program_name = "spotify"  # Программа, которую нужно найти
matching_files = find_program_by_name(program_name)
print(matching_files)
