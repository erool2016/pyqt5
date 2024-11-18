

class Roll:
    """Класс для представления ролика."""

    def __init__(self, production_date, height, weight, product_name):
        self.production_date = production_date  # Дата производства ролика
        self.height = height  # Высота ролика в миллиметрах
        self.weight = weight  # Вес ролика в килограммах
        #self.series = series  # Серия ролика
        self.product_name = product_name  # Наименование товара


class Cell:
    """Класс для представления ячейки."""

    def __init__(self, number, capacity):
        self.number = number  # Номер ячейки
        self.capacity = capacity  # Вместимость ячейки
        # self.contents = {}  # Содержимое ячейки (наименование товара и количество)
        self.contents = []
    # def add_rolls(self, product_name, quantity,date):
    #     """Добавляет ролики в ячейку."""
    #     if product_name in self.contents:
    #         self.contents[product_name] += [quantity,date]  # Увеличиваем количество товара
    #
    #     else:
    #         self.contents[product_name] = [quantity,date]  # Добавляем новый товар

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


# Создание ячеек с заданными характеристиками
cells = [
            Cell(1, 54),
            Cell(2, 50),
        ] + [Cell(i, 48) for i in range(3, 31)] + [
            Cell(101, 42),
            Cell(102, 36)
        ]

# Создание списка товаров из десяти наименований
products = [
    ("Товар A"),
    ("Товар B"),
    ("Товар C"),
    ("Товар D"),
    ( "Товар E"),
    ("Товар F"),
    ("Товар G"),
    ("Товар H"),
    ( "Товар I"),
    ( "Товар J"),
]


def display_all_cells():
    """Выводит информацию обо всех ячейках."""
    print("Все ячейки:")
    list11=[]
    for cell in cells:
        print(cell.get_info())
        list11.append(cell.get_info())
    return list11

def display_filled_cells():
    """Выводит информацию о ячейках, в которых размещены ролики."""
    print("Ячейки с товаром:")
    filled_cells = [cell.get_info() for cell in cells if not cell.is_empty()]

    if filled_cells:
        for info in filled_cells:
            print(info)
    else:
        print("Нет ячеек с товаром.")


def display_empty_cells():
    """Выводит номера пустых ячеек."""
    print("Пустые ячейки:")
    empty_cells = [cell.number for cell in cells if cell.is_empty()]

    if empty_cells:
        print(", ".join(map(str, empty_cells)))
    else:
        print("Нет пустых ячеек.")


def accept_new_rolls():
    """Модуль для добавления новых роликов в ячейки.
    Запрашивает у пользователя наименование товара и количество,
    затем размещает ролики в первой подходящей ячейке.
    """
    print("Добавление новых роликов.")

    # Вывод списка доступных товаров
    print("Доступные товары:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product}")
    # for name in products:
    #     print(name)
    choice = int(input("Выберите номер товара: ")) - 1
    quantity = int(input("Введите количество: "))
    date = input("введите дату (дд.мм.гггг)")

    selected_product = products[choice]

    for cell in cells:
        if cell.can_add_product(selected_product, quantity):  # Проверяем возможность размещения
            cell.add_rolls(selected_product, quantity,date)
            cell.capacity -= quantity
            print(f"Ролики добавлены в ячейку {cell.number}.")
            return


    print("Нет подходящей ячейки для размещения роликов.")

# def main():
#         """Основная функция программы для управления действиями пользователя.
#         Запрашивает у пользователя действие и вызывает соответствующий модуль.
#         """
#         while True:
#             action = input(
#                 "Что вы хотите сделать? (1 - добавить ролики, "
#                 "2 - показать все ячейки с товаром, "
#                 "3 - показать пустые ячейки, "
#                 "4 - посмотреть все ячейки или выйти из программы): "
#             )
#
#             if action == '1':
#                 accept_new_rolls()
#             elif action == '2':
#                 display_filled_cells()
#             elif action == '3':
#                 display_empty_cells()
#             elif action == '4':
#                 display_all_cells()
#             elif action == '0':
#                 break
#         else:
#             print("Неверный ввод. Попробуйте снова.")
#
# if __name__ == "__main__":
#
#     main()
    # window.mainloop()