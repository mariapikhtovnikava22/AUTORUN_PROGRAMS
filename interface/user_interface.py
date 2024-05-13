import os
from tkinter import Tk, Label, Button, Listbox, Scrollbar, Frame
from createDesktopFile.autostart import get_autostart_programs, get_name_and_path
from add_autorun_interface import AddAutorun
from edit_autorun_interface import EditAutorun
from createDesktopFile.autostart import GenerateDesktopFile, find_program_by_name


class UserInterface():
    def __init__(self):
        self.program_list = None
        self.root = Tk()
        self.root.title("AUTORUN CONTROL")
        self.root.resizable(0, 0)
        self.root.geometry("800x400+500+250")
        self.current_list_programs = get_autostart_programs()
        self.create_widgets()

    def create_widgets(self):

        frame = Frame(self.root)
        frame.pack(side="left", fill="y", padx=10, pady=10)

        # Создание виджетов
        header_label = Label(frame, text="Programs in autorun:")
        header_label.pack()
        scrollbar = Scrollbar(frame, orient="vertical")
        self.program_list = Listbox(frame, width=50, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.program_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.program_list.pack(expand=True, fill="both")

        self.show_autostart_files()

        buttons_frame = Frame(self.root)
        buttons_frame.pack(side="right", fill="x", padx=10, pady=10)

        add_button = Button(buttons_frame, text="Add to autorun", command=self.add_to_startup)
        add_button.pack(side="top", pady=10)

        remove_button = Button(buttons_frame, text="Remove from autorun", command=self.remove_from_startup)
        remove_button.pack(side="top", pady=10)

        edit_autostart = Button(buttons_frame, text="Edit autorun files", command=self.edit_autostart_files)
        edit_autostart.pack(side="top", pady=10)

    def edit_autostart_files(self):
        selected_index = self.program_list.curselection()
        if selected_index:
            program = self.program_list.get(selected_index)
            file_path = os.path.join('/home/maria/.config/autostart', find_program_by_name(program)[0])
            name, path = get_name_and_path(file_path)
            print(name, path)
            edit_window = EditAutorun(self.root, name, path)
            edit_window.run()
            self.current_list_programs = get_autostart_programs()
            self.show_autostart_files()

    def show_autostart_files(self):
        self.program_list.delete(0, "end")
        for i in self.current_list_programs:
            self.program_list.insert("end", i)

    def add_to_startup(self):

        add_window = AddAutorun(self.root)
        add_window.run()
        self.current_list_programs = get_autostart_programs()
        self.show_autostart_files()

    def remove_from_startup(self):
        selected_index = self.program_list.curselection()
        if selected_index:
            program = self.program_list.get(selected_index)
            gn = GenerateDesktopFile("", "")
            gn.delete_desktop_file(program, self.root)
            self.current_list_programs = get_autostart_programs()
            self.show_autostart_files()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
