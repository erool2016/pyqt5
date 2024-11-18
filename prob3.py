import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit, \
    QInputDialog

# Список товаров
products = ["Товар 1", "Товар 2", "Товар 3"]
# Список для хранения добавленных роликов
added_rolls = []


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
        btn_show_all.clicked.connect(self.show_all)
        btn_show_empty.clicked.connect(self.show_empty)
        btn_show_full.clicked.connect(self.show_full)
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

    def show_all(self):
        itog = '\n'.join(products + added_rolls)  # Преобразуем список товаров и добавленных роликов в строку
        result = "Все элементы:\n" + itog  # Формируем результат
        self.display_result(result)

    def show_empty(self):
        result = "Показаны пустые элементы."
        self.display_result(result)

    def show_full(self):
        result = "Показаны полные элементы."
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
                # Запрашиваем количество роликов
                quantity, ok3 = QInputDialog.getInt(self, 'Введите количество роликов', 'Количество:', min=1)

                if ok3:
                    # Сохраняем введенные данные в список
                    added_rolls.append(f'{roll_name} - Дата: {production_date}, Количество: {quantity}')
                    self.display_result(f'Добавлено: {roll_name} - Дата: {production_date}, Количество: {quantity}')

    def display_result(self, result):
        self.result_area.append(result)  # Добавляем результат в текстовое поле

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.resize(600, 400)  # Устанавливаем размер окна
    ex.show()
    sys.exit(app.exec_())
