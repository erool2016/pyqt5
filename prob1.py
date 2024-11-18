import sys
from PyQt5.QtWidgets import QApplication, QWidget,QInputDialog, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject
from prob2 import list,show_list,added_rolls
from main import Roll,Cell,cells,products,display_all_cells
from db import insert_data_to_cells, create_table, drop_table, show_all_cells, create_cell_to_table, update_roll, \
    get_info_cell


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Пример PyQt5')

        # Создаем основной layout
        main_layout = QHBoxLayout()

        # Создаем вертикальный layout для кнопок
        button_layout = QVBoxLayout()

        # Создаем кнопки
        btn_show_all = QPushButton('Показать все', self)
        btn_show_empty = QPushButton('Показать пустые', self)
        btn_show_full = QPushButton('Показать полные', self)
        btn_save = QPushButton('Сохранить', self)
        btn_add_roll = QPushButton('Добавить ролики', self)

        # Подключаем кнопки к функциям
        btn_show_all.clicked.connect(self.show_all)
        btn_show_empty.clicked.connect(self.show_empty)
        btn_show_full.clicked.connect(self.show_full)
        btn_save.clicked.connect(self.save)
        btn_add_roll.clicked.connect(self.add_rolls)

        # Добавляем кнопки в вертикальный layout
        button_layout.addWidget(btn_show_all)
        button_layout.addWidget(btn_show_empty)
        button_layout.addWidget(btn_show_full)
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_add_roll)

        # Создаем текстовое поле для отображения результатов
        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)  # Делаем текстовое поле только для чтения

        # Добавляем кнопки и текстовое поле в основной layout
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_area)

        # Устанавливаем основной layout в главное окно
        self.setLayout(main_layout)

    def show_all(self):
        """Выводит информацию обо всех ячейках."""
        self.clear_area()
        result = "\n"
        res = []
        for cell in cells:
            print(f'cell number {cell.number}')
            res.append(get_info_cell(cell.number))

            # print(get_info_cell(cell.number))
            # result += cell.get_info_cell(cell.number) + "\n"
        print(f'show_all {res}')
        for i in res:
            print(i)
            self.display_result(f'{res[0]}{res[1]}')
        # self.display_result(res)
        # itog = '\n'.join(show_list(list))  # Преобразуем список товаров в строку
        # itog = '\n'.join(display_all_cells(products))
        # result = "Все элементы:\n" + itog  # Формируем результат
        # self.display_result(result)




    def show_empty(self):
        """Выводит номера пустых ячеек."""
        result = "Пустые ячейки:\n"
        empty_cells = [cell.number for cell in cells if cell.is_empty()]

        if empty_cells:
            result += ", ".join(map(str, empty_cells))
        else:
            result += "Нет пустых ячеек."

        self.display_result(result)
        # self.clear_area()
        # result = "Показаны пустые элементы."
        # self.display_result(result)

    def show_full(self):
        result = "Показаны полные элементы."
        self.clear_area()
        result = "\n"
        res = []
        for cell in cells:
            # print(f'cell number {cell.number}')
            res.append(get_info_cell(cell.number))

            # print(get_info_cell(cell.number))
            # result += cell.get_info_cell(cell.number) + "\n"
        print(f'show_all {res}')
        for i in res:
            print(i[0][0])

            # print(i)
            #     self.display_result(f'{res[0]}{res[1]}')
        # res = show_all_cells()
        # self.display_result(res[0])
        # print(f'res {res[0]}')

    def save(self):
        result = "Данные сохранены."
        self.display_result(result)

    def display_result(self, result):
        self.result_area.append(result)  # Добавляем результат в текстовое поле

    def clear_area(self):
        self.result_area.clear()

    def add_rolls(self):
        # Запрашиваем название ролика
        roll_name, ok1 = QInputDialog.getItem(self, 'Выберите товар', 'Название товара:', list, 0, False)

        if ok1 and roll_name:
            # Запрашиваем дату производства
            production_date, ok2 = QInputDialog.getText(self, 'Введите дату производства', 'Дата производства:')

            if ok2 and production_date:
                # Запрашиваем количество роликов
                quantity, ok3 = QInputDialog.getInt(self, 'Введите количество роликов', 'Количество:', min=1)

                if ok3:
                    namber_cell, ok4 = QInputDialog.getInt(self, 'Введите номер ячейки,','Номер',min=1)

                    if ok4:
                        # Сохраняем введенные данные в список
                        # added_rolls.append(f'{roll_name} - Дата: {production_date}, Количество: {quantity},number_cell {namber_cell}')
                        added_rolls.append(roll_name)
                        added_rolls.append(production_date)
                        added_rolls.append(quantity)
                        added_rolls.append(namber_cell)
                        print(added_rolls)
                        # insert_data_to_cells(added_rolls)
                        update_roll(roll_name,namber_cell, production_date, quantity)
                        self.display_result(f'Добавлено: {roll_name}  Дата: {production_date}, Количество: {quantity}, Номер ячейки: {namber_cell}'
                                           )
                        self.display_result(f'все ячейки {show_all_cells()}')
                        print(f'все ячейки {show_all_cells()}')





                        # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_F12:
    #         self.close()

if __name__ == '__main__':
    # drop_table()
    # create_table()
    # create_cell_to_table()
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.resize(600, 400)  # Устанавливаем размер окна
    ex.show()
    sys.exit(app.exec_())
