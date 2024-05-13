from tkinter import Label, Button, Frame, Toplevel, Entry, filedialog
from checks.checks import check_add
from createDesktopFile.autostart import GenerateDesktopFile

class EditAutorun:
    def __init__(self, parent, old_name, old_path):
        self.parent = parent
        self.root = Toplevel(self.parent)
        self.root.title("Edit autorun program")
        self.root.transient(parent)

        width = 500
        height = 250
        x = parent.winfo_rootx() + parent.winfo_width() // 2 - width // 2
        y = parent.winfo_rooty() + parent.winfo_height() // 2 - height // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.name = old_name
        self.path = old_path

        self.name_entry = None
        self.file_entry = None

        self.create_widgets()

    def create_widgets(self):
        # Создаем контейнер для всех фреймов
        container = Frame(self.root)
        container.pack(fill="both", expand=True)

        # frame_name
        frame_name = Frame(container)

        label_name = Label(master=frame_name, text="Name:")
        label_name.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = Entry(frame_name)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.name_entry.insert(0, self.name)
        frame_name.grid_columnconfigure(1, weight=1)  # Задаем равный вес для столбца с полем "Name"

        # frame_file
        frame_file = Frame(container)

        label_file_path = Label(master=frame_file, text="Path program:")
        label_file_path.grid(row=0, column=0, padx=5, pady=5)
        self.file_entry = Entry(frame_file)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.file_entry.insert(0, self.path)
        browse_button = Button(frame_file, text="Browse..", command=self.browse_files)
        browse_button.grid(row=0, column=2, padx=5, pady=5)

        frame_file.grid_columnconfigure(1, weight=1)  # Задаем равный вес для столбца с полем "Path program"

        # frame_buttons
        frame_buttons = Frame(container)

        add_button = Button(frame_buttons, text="Edit", command=self.edit_to_startup)
        add_button.pack(side="right", padx=5, pady=5)

        cancel_button = Button(frame_buttons, text="Cancel", command=self.cancel_editions)
        cancel_button.pack(side="right", padx=5, pady=5)

        # Упаковываем все фреймы
        frame_name.pack(fill="x", padx=10, pady=10)
        frame_file.pack(fill="x", padx=10, pady=10)
        frame_buttons.pack(fill="x", padx=10, pady=10)

    def browse_files(self):
        self.root.grab_set()  # Заблокировать другие окна
        file_path = filedialog.askopenfilename(parent=self.root, initialdir='/snap/bin')
        if file_path:
            self.file_entry.delete(0, "end")  # Очистить поле ввода
            self.file_entry.insert(0, file_path)  # Вставить выбранный путь в поле ввода
        self.root.grab_release()  # Разблокировать другие окна после закрытия диалогового окна

    def edit_to_startup(self):

        if not(check_add(self.name_entry.get(), self.file_entry.get(), self.root)):
            self.root.destroy()
        GenerateDesktopFile(self.name_entry.get(), self.file_entry.get())
        self.root.destroy()

    def cancel_editions(self):
        self.root.destroy()

    def run(self):
        self.root.grab_set()
        self.root.wait_window()
        self.root.grab_release()
