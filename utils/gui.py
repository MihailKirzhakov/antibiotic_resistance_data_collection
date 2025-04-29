import customtkinter as ctk
from tkinter import filedialog, messagebox

from .convert_word_to_pdf import convertation
from .get_data_from_pdf import add_to_table
from params.config import settings
from params.constants import (
    PROCESSING, CHOOSE_FILE, CHOOSE_FOLDER, TO_CONVERT,
    TO_COLLECT_PACK, CHOOSE_FILE_ERROR, CHOOSE_FOLDER_ERROR,
    WARNING, NOTIFICATION, FINISHED_PROCESS, ERROR
)


class GraphicalUserInterface:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title('ARDC')
        self.app.geometry('500x500')

        # Пути к файлам
        self.folder_path = None
        self.excel_file_path = None
        if settings.MAIN_EXCEL_FILE_PATH:
            self.folder_path = settings.MAIN_FOLDER_PATH
        if settings.MAIN_EXCEL_FILE_PATH:
            self.excel_file_path = settings.MAIN_EXCEL_FILE_PATH

        # Прогресс-бар с заданной шириной
        self.progress_bar = ctk.CTkProgressBar(self.app, width=200)
        self.progress_label = ctk.CTkLabel(self.app, text=PROCESSING)

        # Определяем ширину кнопок
        self.button_width = max(
            len(TO_CONVERT), len(TO_COLLECT_PACK)
        ) * 10

        # ---------- Кнопки ----------
        # Кнопка выбора файла excel
        self.choose_main_excel_file_button = ctk.CTkButton(
            self.app,
            text=CHOOSE_FILE,
            command=self.choose_main_excel_file,
            width=self.button_width
        )
        self.choose_main_excel_file_button.pack(pady=(50, 5))
        # Поле для вывода пути к файлу
        self.excel_label_frame = ctk.CTkFrame(self.app)
        self.excel_label_frame.pack(pady=(0, 5))
        self.excel_label = ctk.CTkLabel(
            self.excel_label_frame,
            text=(
                self.excel_file_path if self.excel_file_path
                else CHOOSE_FILE_ERROR
            )
        )
        self.excel_label.pack()

        # Кнопка выбора папки с файлами
        self.choose_folder_button = ctk.CTkButton(
            self.app,
            text=CHOOSE_FOLDER,
            command=self.choose_folder,
            width=self.button_width
        )
        self.choose_folder_button.pack(pady=(0, 5))
        # Поле для вывода пути к папке
        self.folder_label_frame = ctk.CTkFrame(self.app)
        self.folder_label_frame.pack(pady=(0, 5))
        self.folder_label = ctk.CTkLabel(
            self.folder_label_frame,
            text=(
                self.folder_path if self.folder_path
                else CHOOSE_FOLDER_ERROR
            )
        )
        self.folder_label.pack(pady=(0, 5))

        # Кнопка для запуска конвертирования
        self.convert_button = ctk.CTkButton(
            self.app,
            text=TO_CONVERT,
            command=self.on_convert,
            width=self.button_width
        )
        self.convert_button.pack(pady=(0, 5))

        # Кнопка для запуска обработки и упаковки данных
        self.add_button = ctk.CTkButton(
            self.app,
            text=TO_COLLECT_PACK,
            command=self.on_add,
            width=self.button_width
        )
        self.add_button.pack(pady=(0, 5))

    def choose_main_excel_file(self):
        self.excel_file_path = filedialog.askopenfilename(
            title=CHOOSE_FILE,
            filetypes=(('Excel files', '*.xlsx;*.xls'),)
        )
        if self.excel_file_path:
            self.excel_label.configure(text=self.excel_file_path)
        else:
            self.excel_label.configure(text=CHOOSE_FILE_ERROR)

    def choose_folder(self):
        self.folder_path = f'{filedialog.askdirectory(title=CHOOSE_FOLDER)}/'
        if self.folder_path:
            self.folder_label.configure(text=self.folder_path)
        else:
            self.folder_label.configure(text=CHOOSE_FOLDER_ERROR)

    def on_convert(self):
        if not self.folder_path:
            messagebox.showwarning(WARNING, CHOOSE_FOLDER_ERROR)
            return

        self.choose_folder_button.configure(state='disabled')
        self.choose_main_excel_file_button.configure(state='disabled')
        self.convert_button.configure(state='disabled')
        self.add_button.configure(state='disabled')
        self.progress_label.pack(pady=(5, 5))
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        self.app.update()
        try:
            convertation(self.folder_path, self.update_progress)
        except Exception as e:
            messagebox.showerror(ERROR, e)
        finally:
            self.choose_folder_button.configure(state='normal')
            self.choose_main_excel_file_button.configure(state='normal')
            self.convert_button.configure(state='normal')
            self.add_button.configure(state='normal')
            self.progress_bar.pack_forget()
            self.progress_label.pack_forget()
            messagebox.showwarning(NOTIFICATION, FINISHED_PROCESS)

    def on_add(self):
        if not self.excel_file_path:
            messagebox.showwarning(WARNING, CHOOSE_FILE_ERROR)
            return

        self.choose_folder_button.configure(state='disabled')
        self.choose_main_excel_file_button.configure(state='disabled')
        self.convert_button.configure(state='disabled')
        self.add_button.configure(state='disabled')
        self.progress_label.pack(pady=(5, 5))
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        self.app.update()
        try:
            add_to_table(self.excel_file_path, self.update_progress)
        except Exception as e:
            messagebox.showerror(ERROR, e)
        finally:
            self.choose_folder_button.configure(state='normal')
            self.choose_main_excel_file_button.configure(state='normal')
            self.convert_button.configure(state='normal')
            self.add_button.configure(state='normal')
            self.progress_bar.pack_forget()
            self.progress_label.pack_forget()
            messagebox.showwarning(NOTIFICATION, FINISHED_PROCESS)

    def update_progress(self, progress):
        self.progress_bar.set(progress)
        self.app.update()

    def run(self):
        self.app.mainloop()


gui_app = GraphicalUserInterface()
