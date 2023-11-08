import tkinter as tk

from arnion.db.mysql_connection import ConnectionHandler


class MainWindow:
    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(text="SPAN", font=('Helvetica', 10, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=15, width=250, height=50)

        lblTitle1 = tk.Label(text="Данные", font=('Helvetica', 10, 'bold'), fg='#0000cc', justify='center')
        lblTitle1.place(x=25, y=55, width=250, height=50)

        # -------------------------------------------------------------

        # Добавление метки "Отчёты"
        lbl_title = tk.Label(text="Отчёты", font=('Helvetica', 10, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки данных "Отделы"
        btn_report = tk.Button(self.window, text="Отделы", font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_report = tk.Button(self.window, text="Сотрудники", font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=160, y=200, width=120, height=50)

        # Добавление кнопки данных "Отделы"
        btn_report = tk.Button(self.window, text="Отделы", font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_report = tk.Button(self.window, text="Сотрудники", font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=160, y=100, width=120, height=50)

        # Добавление кнопки Тест
        btn_close = tk.Button(self.window, text="Тест", font=('Helvetica', 10, 'bold'), bg='#ffffcc', command=self.do_test)
        btn_close.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text="Выход", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция Тест
    def do_test(self):
        ch = ConnectionHandler()
        ch.do_test()

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()