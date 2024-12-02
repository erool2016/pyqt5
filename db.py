import psycopg2

import main


data = [['name1',25],['name2',35]]
def drop_table():# Удаляем таблицы cells,goods
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                DROP TABLE IF EXISTS cells CASCADE;
    
                            '''
                        )
            print('удалена таблица cell')
        with conn.cursor() as cur:
            cur.execute('''
                                drop table goods;

                            '''
                        )
            print('удалена таблица goods')
        # conn.commit()
    except Exception as _e:

        print(f'error connction, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('conect drop closed')

def create_table(): #Создаем таблицы cells,goods
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT version();'
            )
            print(f'server version {cursor.fetchone()}')
        with conn.cursor() as cursor:
            cursor.execute(
                           '''CREATE TABLE if not exists cells(
                           id serial PRIMARY KEY,
                           number integer unique
                           )'''
            )
            # conn.commit()
            print(f'table cells - created')
        with conn.cursor() as cursor:
            cursor.execute(
                           '''CREATE TABLE if not exists goods(
                           id serial PRIMARY KEY,
                           prod_name varchar(50) NOT NULL,
                           prod_date varchar(50),
                           quantity integer NOT NULL,
                           cells_number int not null,
                           FOREIGN KEY (cells_number) REFERENCES cells (number)
                           )'''
            )
            # conn.commit()
            print(f'table goods - created')
    except Exception as _e:

        print(f'error connction, {_e}')
    finally:
        if conn:
            cursor.close()
            conn.close()
            print('conect create closed')

def create_cell_to_table():
    print(f'create cell to table')
    print(main.cells)
    for cell in main.cells:
        # print(cell.get_info())
        data=['noname','1000.01.01',00]
        insert_data_to_cells(data,cell.number)

def insert_data_to_cells(data): # Вносит данные в ячейку
    # print(data)
    # print(f'данные получены  {type(data[0])} {type(data[1])}{type(data[3])} тип {type(data[2])}')
    if check_cell(data[3]):
        try:
            conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
            conn.autocommit = True

            with conn.cursor() as cur:
                cur.execute('''
                                INSERT INTO goods (prod_name, prod_date, quantity, cells_number) 
                                VALUES (%s, %s, %s, %s)
                                RETURNING id;
                            ''', (data[0], data[1], data[2], data[3]))
                print(f'данные внесены name {data[0]} prod_data {data[1]} quant {data[2]} cell {data[3]}')

        except Exception as _e:

            print(f'insert not added, {_e}')
        finally:
            if conn:
                cur.close()
                conn.close()
                print('conect insert closed')
    else:
        create_cell(data[3])
        insert_data_to_cells(data)

def create_cell(number):  # Создает ячейку
    print(number)
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO cells (number) 
                        VALUES (%s);
                    ''', (number,))
            print(f'создана ячейка номер- {number}')
    except Exception as _e:

        print(f'cell not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('cell  closed')

def check_cell(number): # Проверка на существование ячейки
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute('''
                        SELECT * from cells
                         WHERE number = %s;
                    ''', (number,))
            res = cur.fetchall()
            # print(f'данные внесены name {data[0]} prod_data {data[1]} quant {data[2]}')

    except Exception as _e:

        print(f'cell not find, {_e}')

    finally:
        if conn:
            # cur.close()
            conn.close()
            print('check cell  closed')
            print(res)
            if res == []:
                return False
            return True

def update_roll(prod_name,number_cell, data, quantity):
    """Обновляет данные о ролике в таблице cells по номеру ячейки."""
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE cells 
                SET prod_name = %s, prod_date = %s,quantity = %s 
                WHERE id = %s
            """, (prod_name,data, quantity, number_cell))
            print(f'данные внесены наименование{prod_name}\n дата {data}\n количество {quantity}\n ячейка {number_cell}')
            # connection.commit()
    except Exception as _e:

        print(f'insert not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('conect insert closed')
# def show_all_cells():
#     ''' Показывает все полные ячейка'''
#     try:
#         conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
#         conn.autocommit = True
#         with conn.cursor() as cur:
#             cur.execute('''
#                                   select * from cells;
#
#                               ''',)
#             # conn.commit()
#             ant = cur.fetchall()
#             # print(f'данные show_all_cells {ant}')
#             return ant
#
#     except Exception as _e:
#
#         print(f'show not added, {_e}')
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
            # print('conect closed')
def get_info_cell(cell_number):
    # print(f'cell_number {cell_number} of get info cell')
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                  select * from cells where id = %s; 

                              ''',(cell_number,))
            # conn.commit()
            ant = cur.fetchall()
            # print(f'данные get_info_cells {ant[0]}')
            return ant

    except Exception as _e:

        print(f'show not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            # print('conect get_info_cell closed')

def get_info_goods(cell_number):
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                  select * from goods where cells_number = %s; 

                              ''',(cell_number,))
            # conn.commit()
            ant = cur.fetchall()
            # print(f'данные get_info_cells {ant[0]}')
            return ant

    except Exception as _e:

        print(f'show not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            # print('conect get_info_goods closed')

def get_all_info(): # Получаем информацию о ячейках и их содержимом
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute('''
                        SELECT cells.number, goods.prod_name,goods.prod_date,goods.quantity from cells
                         join goods ON cells.number=goods.cells_number;
                    ''', )
            res = cur.fetchall()
            # print(f'данные внесены name {data[0]} prod_data {data[1]} quant {data[2]}')

    except Exception as _e:

        print(f'cell not find, {_e}')

    finally:
        if conn:
            # cur.close()
            conn.close()
            # print('show all info  closed')
            # print(res)
            return res

# def get_info_goods(cell_number):
#     # print(f'cell_number {cell_number} of get info cell')
#     try:
#         conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
#         conn.autocommit = True
#         with conn.cursor() as cur:
#             cur.execute('''
#                                   select * from goods where id = %s;
#
#                               ''',(cell_number,))
#             # conn.commit()
#             ant = cur.fetchall()
#             # print(f'данные get_info_cells {ant[0]}')
#             return ant
#
#     except Exception as _e:
#
#         print(f'show not added, {_e}')
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# if __name__ == '__main__':
#     # create_cell_to_table()
#     # update_roll('prod_1',11,'2024.07.25',33)
#     update_roll('prod_4', 3, '2024.12.23', 12)
#     drop_table()
#     create_table()
# #     for item in data:
# #         insert_data_to_cells(item)
# #     print(show_all_cells())