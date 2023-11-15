import tkinter as tk

from arnion.data.employees_data import EmployeeDataHandler, EmployeeDataObject
from arnion.ui.departmens_data_ui import DepartmentsWindow
from arnion.ui.departmens_repots_ui import DepartmentsReportWindow
from arnion.ui.employee_data_ui import EmployeesWindow
from arnion.ui.employees_repots_ui import EmployeesReportWindow

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
        btn_report = tk.Button(self.window, text="Отделы", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_departments)
        btn_report.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_report = tk.Button(self.window, text="Сотрудники", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_employees)
        btn_report.place(x=160, y=200, width=120, height=50)

        # Добавление кнопки данных "Отделы"
        btn_report = tk.Button(self.window, text="Отделы", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_list_departments)
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_report = tk.Button(self.window, text="Сотрудники", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_list_employees)
        btn_report.place(x=160, y=100, width=120, height=50)

        # Добавление кнопки Тест
        btn_close = tk.Button(self.window, text="Тест", font=('Helvetica', 10, 'bold'), bg='#ffffcc', command=self.do_test)
        btn_close.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text="Выход", font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция Тест
    def do_test(self):
        employee = EmployeeDataObject(first_name="Вера", middle_name="Михайловна", last_name="Янова", department_id=1)
        print(employee.employee_id)
        EmployeeDataHandler.insert(employee)
        print(employee.employee_id)
        print("Готово")

    # Открытие списка Отделы
    def do_list_departments(self):
        rpt = DepartmentsWindow()
        rpt.open()

    # Открытие списка Сотрудники
    def do_list_employees(self):
        rpt = EmployeesWindow()
        rpt.open()


    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()