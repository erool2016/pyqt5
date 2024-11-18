import psycopg2

import main

# class Database:
#     def __init__(self, dbname, user, password, host='localhost', port='5432'):
#         self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
#         self.cursor = self.connection.cursor()
#
#     def create_table(self):
#         """Создает таблицу cells."""
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS cells (
#                 id SERIAL PRIMARY KEY,
#                 number_cell INTEGER NOT NULL,
#                 product_name VARCHAR(255),
#                 data DATE,
#                 quantity INTEGER
#             )
#         """)
#         self.connection.commit()
#
#     def drop_table(self):
#         """Удаляет таблицу cells."""
#         self.cursor.execute("DROP TABLE IF EXISTS cells")
#         self.connection.commit()
#
#     def insert_roll(self, number_cell, product_name, data, quantity):
#         """Вставляет данные о ролике в таблицу cells."""
#         self.cursor.execute("""
#             INSERT INTO cells (number_cell, product_name, data, quantity)
#             VALUES (%s, %s, %s, %s)
#         """, (number_cell, product_name, data, quantity))
#         self.connection.commit()
#
#     def close(self):
#         """Закрывает соединение с базой данных."""
#         self.cursor.close()
#         self.connection.close()
#
# def create_table():
#     Database.create_table(self=)
#     print('table created')
#
# create_table()

# DSN = 'postgresql://postgres:qwr1d@localhost:5432/postgres'  # адрес базы
# engine = sqlalchemy.create_engine(DSN)  # создаем движок


# try:
#
#     conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
#     conn.autocommit = True
#     with conn.cursor() as cursor:
#         cursor.execute(
#                        'SELECT version();'
#         )
#         print(f'server version {cursor.fetchone()}')
#     # with conn.cursor() as cursor:
#     #     cursor.execute(
#     #                    '''CREATE TABLE cells(
#     #                    id serial PRIMARY KEY,
#     #                    prod_name varchar(50) NOT NULL,
#     #                    quantity integer NOT NULL
#     #                    )'''
#     #     )
#     #     # conn.commit()
#     #     print(f'table cells - created')
#     with conn.cursor() as cursor:
#         cursor.execute(
#             '''INSERT INTO cells(prod_name,quantity) VALUES
#             ('name1',12);'''
#         )
#         # conn.commit()
#         print(f'table added')
# except Exception as _e:
#
#     print(f'error connction, {_e}')
# finally:
#     if conn:
#         cursor.close()
#         conn.close()
#         print('conect closed')

# Session = sessionmaker(bind=engine)
data = [['name1',25],['name2',35]]
def drop_table():
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                drop table cells;
    
                            '''
                        )
            print('удалена таблица cell')
        # conn.commit()
    except Exception as _e:

        print(f'error connction, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('conect drop closed')

def create_table():
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
                           prod_name varchar(50) NOT NULL,
                           prod_date date,
                           quantity integer NOT NULL
                           )'''
            )
            # conn.commit()
            print(f'table cells - created')
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

def insert_data_to_cells(data,number_cell):
    print(f'данные получены {data[0]} {data[1]} {number_cell}')
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                  insert into cells(prod_name,prod_date,quantity) 
                                  values(%s,%s,%s); 

                              ''', (data[0], data[1],data[2]))
            conn.commit()
            print(f'данные внесены name {data[0]} prod_data {data[1]} quant {data[2]}')
    except Exception as _e:

        print(f'insert not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('conect insert closed')

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
def show_all_cells():
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('''
                                  select * from cells; 

                              ''',)
            # conn.commit()
            ant = cur.fetchall()
            print(f'данные show_all_cells {ant}')
            return ant

    except Exception as _e:

        print(f'show not added, {_e}')
    finally:
        if conn:
            cur.close()
            conn.close()
            print('conect closed')
def get_info_cell(cell_number):
    print(f'cell_number {cell_number} of get info cell')
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
            print('conect get_info_cell closed')

# if __name__ == '__main__':
#     # create_cell_to_table()
#     # update_roll('prod_1',11,'2024.07.25',33)
#     update_roll('prod_4', 3, '2024.12.23', 12)
# #     # drop_table()
# #     # create_table()
# #     for item in data:
# #         insert_data_to_cells(item)
# #     print(show_all_cells())