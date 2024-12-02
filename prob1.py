import sys
from PyQt5.QtWidgets import QApplication, QWidget,QInputDialog, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject
from datetime import datetime

from prob2 import list,show_list,added_rolls
from main import Roll,Cell,cells,products,display_all_cells
from db import insert_data_to_cells, create_table, drop_table, create_cell_to_table, update_roll, \
    get_info_cell, get_all_info, get_info_goods # , show_all_cells


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
        btn_shipment = QPushButton('Отгрузить ролики',self)

        # Подключаем кнопки к функциям
        btn_show_all.clicked.connect(self.show_all) #  связано с функцией показать ВСЕ
        btn_show_empty.clicked.connect(self.show_empty) #  связано с функцией показать ПУСТЫЕ
        btn_show_full.clicked.connect(self.show_full) #  связано с функцией показать ПОЛНЫЕ
        btn_save.clicked.connect(self.save)
        btn_add_roll.clicked.connect(self.add_rolls) #  связано с функцией показать ДОБАВЛЕНИЯ
        btn_shipment.clicked.connect(self.shipment_rolls) #  связано с функцией показать ОТГРУЗКИ

        # Добавляем кнопки в вертикальный layout
        button_layout.addWidget(btn_show_all)
        button_layout.addWidget(btn_show_empty)
        button_layout.addWidget(btn_show_full)
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_add_roll)
        button_layout.addWidget(btn_shipment)

        # Создаем текстовое поле для отображения результатов
        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)  # Делаем текстовое поле только для чтения

        # Добавляем кнопки и текстовое поле в основной layout
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_area)

        # Устанавливаем основной layout в главное окно
        self.setLayout(main_layout)



    def create_string_show_full(self,my_dict):
        print('-------', my_dict)
        res = '\n'
        for key, value in my_dict.items():
            if len(value) > 1:
                res += (f'ячейка {key} содержит \n')

                for i in value:
                    print(key, i)
                    res += (
                        f'{i[0]} '
                        f'{i[1]} '
                        f'{i[2]}\n'
                    )
            else:
                res += (f'ячейка {key} содержит {value[0][0]}\n')
        print(res)
        return res

    def upload_data(self)->dict:# Загружаем данные обо всех заполненных ячейках
        res = get_all_info()
        # print(res)
        my_dict = {}

        for item in res:
            # print(item)
            name = str(item[0])  # Извлекаем строковое значение из индекса 1
            values = [item[1], item[2], item[3]]  # Создаем список с элементом из индекса 2
            # my_dict[name] = []
            if name in my_dict.keys():

                my_dict[name] += [values]  # Добавляем новые значения к существующему списку
            else:
                my_dict[name] = [values]  # Создаем новый список для нового имени

        # print(my_dict)
        return my_dict

    def show_full(self):# Подготавливает и выводит содержимое  всех заполненных ячеек
        self.clear_area()
        dict_= self.upload_data()
        self.display_result(self.create_string_show_full(dict_))

    def create_string_show_all(self,key: str, item: list) -> str:
        res = (f'ячейка {key} \n')
        # print(f'key {key} item {item}')
        if len(item) > 1:

            for i in item:
                res += (
                    f'{i[0]}\n'
                    f'{i[1]}\n'
                    f'{i[1]}\n'
                )
        else:
            res += (
                f'{item[0][0]}\n'
                f'{item[0][1]}\n'
                f'{item[0][1]}\n'
            )
        return res

        # print(cell.number)

    def show_all(self):
        my_dict = self.upload_data()
        print(my_dict)
        res = '\n'
        for cell in cells:
            if str(cell.number) in my_dict.keys():  # Если ячейка заполнена
                print(self.create_string_show_all(cell.number, my_dict[str(cell.number)]))
                res += self.create_string_show_all(cell.number, my_dict[str(cell.number)])
                # print(cell.number)
                # print(my_dict[str(cell.number)])
                # if len(my_dict[str(cell.number)]) > 1:
                #     create_string_show_all(cell.number,my_dict[str(cell.number)])
                # else:
                #     res += (f'ячейка {cell.number}\n')
            else:
                res += (f'ячейка {cell.number} пустая \n')
        print(res)
        self.display_result(res)

    def sorted_data(self,data)->list:
        def date_key(item):
            return datetime.strptime(item[2], '%Y.%m.%d')

        sorted_list = sorted(data, key=date_key)
        print('отсортированный список',sorted_list)
        return sorted_list

    def proposal_for_shipment(self,item:list,name:str,quantity:int):# Формируем предложение для отгрузки
        print(item)
        need = 0
        for i in item:
            if quantity < i[3] :
                i[3] -= quantity

            else:
                i[3] = 0
                quantity -= i[3]
                continue
        print(item)


    def shipment_rolls(self):# Отгрузка роликов, определение
        list_for_sort =[]
        roll_name, ok1 = QInputDialog.getItem(self, 'Выберите товар', 'Название товара:', list, 0, False)
        if ok1 and roll_name:
            quantity, ok2 = QInputDialog.getInt(self, 'Введите количество','Количество', min=1)
            if ok2 and quantity:
                self.display_result(f'{roll_name},{quantity}')
                my_dict = self.upload_data()
                print(my_dict)
                for key,value in my_dict.items():
                    for item in value:
                        if item[0] == roll_name:
                            print(key,item)
                            list_ =[key,item[0],item[1],item[2]]
                            list_for_sort+=[list_]
        print(list_for_sort)
        item_for_shipment = self.sorted_data(list_for_sort)
        self.proposal_for_shipment(item_for_shipment,roll_name,quantity)








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



    # def show_full(self):
    #     """Выводит информацию обо всех заполненых ячейках и их содержимом."""
    #     result = get_all_info()
    #     print('result show full ',result)
    #     for item in result:
    #         self.display_result(f' ячейка {item[0]} содержит товар  {item[1]} от {item[2]} в количестве {item[3]}')


        # self.clear_area()
        # result = "\n"
        # res = []
        # for cell in cells:
        #     # print(f'cell number {cell.number}')
        #     res.append(get_info_cell(cell.number))
        #
        #     # print(get_info_cell(cell.number))
        #     # result += cell.get_info_cell(cell.number) + "\n"
        # print(f'show_full {res}')
        # for i in res:
        #     print(i)
        #     if i != []:
        #         self.display_result(f'{res[0]}{res[1]}')
        #     else:
        #         self.display_result(f'ячейка {res[0]} - ПУСТАЯ')

    def save(self):
        result = "Данные сохранены."
        self.display_result(result)

    def display_result(self, result): #Отправляем результат в окно вывода программы
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
                        insert_data_to_cells(added_rolls)
                        # update_roll(roll_name,namber_cell, production_date, quantity)
                        self.display_result(f'Добавлено: {roll_name}  Дата: {production_date}, Количество: {quantity}, Номер ячейки: {namber_cell}'
                                           )
                        # self.display_result(f'все ячейки {show_all_cells()}')
                        # print(f'все ячейки {show_all_cells()}')





                        # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_F12:
    #         self.close()

if __name__ == '__main__':
    # drop_table()
    # create_table()
    # create_cell_to_table()
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.resize(800, 600)  # Устанавливаем размер окна
    ex.show()
    sys.exit(app.exec_())
