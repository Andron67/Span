import tkinter as tk
from tkinter import messagebox as mb

from arnion.data.departments_data import DepartmentDataHandler, DepartmentDataObject

class DepartmentsWindow:
    # Конструктор
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("500x500")
        self.window.title("Отделы")

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window, text="Отделы", font=('Helvetica', 16, 'bold'), fg="#0000cc", justify='center')
        lbl_title.place(x=25, y=15, width=450, height=50)

        # Контейнер для списка и полосы прокрутки
        self.frame = tk.Frame(self.window)

        # Добавления списка записей
        self.lbox_data_rows = tk.Listbox(self.frame, selectmode='single', activestyle='none', font=('Courier New', 10, 'bold'))
        self.lbox_data_rows.place(x=0, y=0, width=450, height=300)

        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.config(command=self.lbox_data_rows.yview)
        self.scrollbar.place(x=450, y=0, width=20, height=300)

        self.lbox_data_rows.config(yscrollcommand=self.scrollbar.set)

        self.init_data_rows()
        self.frame.place(x=15, y=75, width=470, height=300)

        # Добавление кнопки Добавить
        self.btn_add = tk.Button(self.window, text='Добавить', font=('Helvetica', 10, 'bold'), bg='#ccccff', command=self.add_record)
        self.btn_add.place(x=20, y=390, width=90, height=30)

        # Добавление кнопки Изменить
        self.btn_edit = tk.Button(self.window, text='Изменить', font=('Helvetica', 10, 'bold'), bg='#ccccff', command=self.edit_record)
        self.btn_edit.place(x=120, y=390, width=90, height=30)

        # Добавление кнопки Удалить
        self.btn_delete = tk.Button(self.window, text='Удалить', font=('Helvetica', 10, 'bold'), bg='#ccccff', command=self.delete_record)
        self.btn_delete.place(x=220, y=390, width=90, height=30)

        # Добавление кнопки закрытие окна
        self.btn_close = tk.Button(self.window, text='Закрыть', font=('Helvetica', 10, 'bold'), bg='#ccccff', command=self.close)
        self.btn_close.place(x=390, y=390, width=90, height=30)

    # Функция заполнения списка
    def init_data_rows(self):
        self.data_rows = DepartmentDataHandler.select_list()
        for data_row in self.data_rows:
            self.lbox_data_rows.insert('end', data_row.department_name)
        if len(self.data_rows) > 0:
            self.lbox_data_rows.select_set(0)

    # Функция добавления записи
    def add_record(self):
        pass

    # Функция завершения добавления записи
    def add_record_callback(self, added_data_row):
        pass

    # Функция редактирования записи
    def edit_record(self):
        pass

    # Функция завершения редактирования записи
    def edit_record_callback(self, edited_data_row):
        pass

    # Функция удаления записи
    def delete_record(self):
        answer = mb.askyesno(parent=self.window, title='Подтверждение', message='Вы действительно хотите удалить запись?')
        if not answer:
            return
        self.selection = self.lbox_data_rows.curselection()[0]
        id = self.data_rows[self.selection].department_id
        DepartmentDataHandler.delete_by_id(id)
        self.data_rows.pop(self.selection)
        self.lbox_data_rows.delete(self.selection)

    # Функция обновления списка
    def refresh_list_box(self, selection:int, value:str):
        pass

    # Функция открытия окна
    def open(self):
        # Перевод фокуса на создание окна
        self.window.focus_force()
        # Перевод всех команд на создание окна
        self.window.grab_set()

    def close(self):
        self.window.destroy()



