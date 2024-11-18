import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit, QInputDialog

class Roll:
    """Класс для представления ролика."""
    def __init__(self, production_date, height, weight, product_name):
        self.production_date = production_date  # Дата производства ролика
        self.height = height  # Высота ролика в миллиметрах
        self.weight = weight  # Вес ролика в килограммах
        self.product_name = product_name  # Наименование товара


class Cell:
    """Класс для представления ячейки."""
    def __init__(self, number, capacity):
        self.number = number  # Номер ячейки
        self.capacity = capacity  # Вместимость ячейки
        self.contents = {}  # Содержимое ячейки (наименование товара и количество)

    def add_rolls(self, product_name, quantity, date):
        """Добавляет ролики в ячейку."""
        if product_name in self.contents:
            self.contents[product_name][0] += quantity  # Увеличиваем количество товара
        else:
            self.contents[product_name] = [quantity, date]  # Добавляем новый товар

    def get_info(self):
        """Возвращает информацию о ячейке и её содержимом."""
        return f"Ячейка {self.number}: {self.contents}"

    def is_empty(self):
        """Проверяет, пуста ли ячейка."""
        return len(self.contents) == 0

    def can_add_product(self, product_name, quantity):
        """Проверяет возможность добавления товара в ячейку."""
        if self.capacity < quantity:  # Проверка на вместимость
            return False
        if len(self.contents) >= 2 and product_name not in self.contents:  # Не более двух наименований товара
            return False
        return True


# Создание списка ячеек
cells = [
    Cell(1, 54),
    Cell(2, 50),
] + [Cell(i, 48) for i in range(3, 31)] + [
    Cell('Торец1', 42),
    Cell('Торец2', 36)
]

# Создание списка товаров из десяти наименований
products = [
    "Товар A", "Товар B", "Товар C", "Товар D",
    "Товар E", "Товар F", "Товар G", "Товар H",
    "Товар I", "Товар J"
]


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
        btn_clear = QPushButton('Очистить', self)  # Кнопка для очистки текстового поля
        btn_add_rolls = QPushButton('Добавить ролики', self)  # Кнопка для добавления роликов

        # Подключаем кнопки к функциям
        btn_show_all.clicked.connect(self.display_all_cells)
        btn_show_empty.clicked.connect(self.display_empty_cells)
        btn_show_full.clicked.connect(self.display_filled_cells)
        btn_save.clicked.connect(self.save)
        btn_clear.clicked.connect(self.clear_text)  # Подключаем кнопку очистки
        btn_add_rolls.clicked.connect(self.add_rolls)  # Подключаем кнопку добавления роликов

        # Добавляем кнопки в вертикальный layout
        button_layout.addWidget(btn_show_all)
        button_layout.addWidget(btn_show_empty)
        button_layout.addWidget(btn_show_full)
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_clear)  # Добавляем кнопку очистки
        button_layout.addWidget(btn_add_rolls)  # Добавляем кнопку добавления роликов

        # Создаем текстовое поле для отображения результатов
        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)  # Делаем текстовое поле только для чтения

        # Добавляем кнопки и текстовое поле в основной layout
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_area)

        # Устанавливаем основной layout в главное окно
        self.setLayout(main_layout)

    def display_all_cells(self):
        """Выводит информацию обо всех ячейках."""
        result = "Все ячейки:\n"
        for cell in cells:
            result += cell.get_info() + "\n"
        self.display_result(result)

    def display_filled_cells(self):
        """Выводит информацию о ячейках, в которых размещены ролики."""
        result = "Ячейки с товаром:\n"
        filled_cells = [cell.get_info() for cell in cells if not cell.is_empty()]

        if filled_cells:
            result += "\n".join(filled_cells)
        else:
            result += "Нет ячеек с товаром."

        self.display_result(result)

    def display_empty_cells(self):
        """Выводит номера пустых ячеек."""
        result = "Пустые ячейки:\n"
        empty_cells = [cell.number for cell in cells if cell.is_empty()]

        if empty_cells:
            result += ", ".join(map(str, empty_cells))
        else:
            result += "Нет пустых ячеек."

        self.display_result(result)

    def save(self):
        result = "Данные сохранены."
        self.display_result(result)

    def clear_text(self):
        self.result_area.clear()  # Очищаем текстовое поле

    def add_rolls(self):
        # Запрашиваем название ролика
        roll_name, ok1 = QInputDialog.getItem(self, 'Выберите товар', 'Название товара:', products, 0, False)

        if ok1 and roll_name:
            # Запрашиваем дату производства
            production_date, ok2 = QInputDialog.getText(self, 'Введите дату производства', 'Дата производства:')

            if ok2 and production_date:
                # Запрашиваем высоту и вес ролика
                height, ok3 = QInputDialog.getInt(self, 'Введите высоту ролика', 'Высота (мм):', min=1)
                weight, ok4 = QInputDialog.getDouble(self, 'Введите вес ролика', 'Вес (кг):', min=0.1)

                if ok3 and ok4:
                    roll = Roll(production_date, height, weight, roll_name)

                    # Запрашиваем номер ячейки для добавления роликов
                    cell_number, ok5 = QInputDialog.getInt(self, 'Введите номер ячейки', 'Номер ячейки:', min=1)

                    if ok5 and (cell_number <= len(cells)):
                        quantity, ok6 = QInputDialog.getInt(self, 'Введите количество роликов', 'Количество:', min=1)

                        if ok6:
                            cell = cells[cell_number - 1]  # Получаем ячейку по номеру

                            if cell.can_add_product(roll.product_name, quantity):
                                cell.add_rolls(roll.product_name, quantity, roll.production_date)
                                self.display_result(
                                    f'Добавлено: {quantity} {roll.product_name} в ячейку {cell_number}.')
                            else:
                                self.display_result(f'Не удалось добавить {roll.product_name} в ячейку {cell_number}.')

    def display_result(self, result):
        self.result_area.append(result)  # Добавляем результат в текстовое поле


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.resize(600, 400)  # Устанавливаем размер окна
    ex.show()
    sys.exit(app.exec_())
