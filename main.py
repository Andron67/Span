import tkinter as tk
from tkinter import messagebox as mb

from arnion.db.mysql_connection import my_connection_handler
from arnion.ui.main_window import MainWindow


# Точка входа в программу
def main():

    chk = my_connection_handler.check_connection()
    if not chk:
        root = tk.Tk()
        root.withdraw()
        mb.showerror(parent=None, title="Ошибка", message="Отсутствует соединение с MySQL сервером")
        return

    main_window = MainWindow()
    main_window.start_mainloop()

    return 0

if __name__ == '__main__':
    main()