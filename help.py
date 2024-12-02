
import datetime,pprint
from datetime import datetime
from db import get_all_info
from main import cells


import psycopg2

def insert_data_to_cells(data):
    print(data)
    print(f'данные получены  {type(data[0])} {type(data[1])}{type(data[3])} тип {type(data[2])}')
    if check_cell(data[3]):
        try:
            conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')
            conn.autocommit = True

            with conn.cursor() as cur:
                cur.execute('''
                            INSERT INTO goods (prod_name, prod_date, quantity, cells_number) 
                            VALUES (%s, %s, %s, %s)
                            RETURNING id;
                        ''', (data[0], data[1],data[2],data[3]))
                print(f'данные внесены name {data[0]} prod_data {data[1]} quant {data[2]} cell {data[3]}')

        except Exception as _e:

            print(f'insert not added, {_e}')
        finally:
            if conn:
                cur.close()
                conn.close()
                print('conect insert closed')
    else:
        print('not found cell')
        create_cell(data[3])
        insert_data_to_cells(data)


def create_cell(number):# Создает ячейку
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

def show_all():
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
            print('show all  closed')
            print(res)


def upload_data():
    res = get_all_info()
    # print(res)
    my_dict = {}

    for item in res:
        # print(item)
        name = str(item[0])  # Извлекаем строковое значение из индекса 1
        values = [item[1],item[2],item[3]]  # Создаем список с элементом из индекса 2
        # my_dict[name] = []
        if name in my_dict.keys():

            my_dict[name]+=[values]  # Добавляем новые значения к существующему списку
        else:
            my_dict[name] = [values]  # Создаем новый список для нового имени

    # print(my_dict)
    return my_dict





def show_full(my_dict):
    print('-------',my_dict)
    res ='\n'
    for key, value in my_dict.items():
        if  len(value) > 1:
            res+=(f'ячейка {key} содержит \n')

            for i in value:
                print(key,i)
                res += (
                    f'{i[0]} '
                    f'{i[1]} '
                    f'{i[2]}\n'
                        )
        else:
            res+=(f'ячейка {key} содержит {value[0][0]}\n')
    print(res)


    # for key, value in my_dict.items():
    #     idx = int(len(value)/3)
    #     # print(f' key {key} idx {idx} value {value}')
    #     create_string(idx,key,value)

def create_string_show_all(key:str,item:list)->str:
    res = (f'ячейка {key} \n')
    # print(f'key {key} item {item}')
    if len(item) >1:

        for i in item:
            res +=(
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
def show_all(my_dict):
    print(my_dict)
    res = '\n'
    for cell in cells:
        if str(cell.number) in my_dict.keys():# Если ячейка заполнена
            print(create_string_show_all(cell.number,my_dict[str(cell.number)]))
            # print(cell.number)
            # print(my_dict[str(cell.number)])
            # if len(my_dict[str(cell.number)]) > 1:
            #     create_string_show_all(cell.number,my_dict[str(cell.number)])
            # else:
            #     res += (f'ячейка {cell.number}\n')
        else:
            res += (f'ячейка {cell.number} пустая \n')
    print(res)

    # for key,item in my_dict.items():
    #     create_string_show_all(key,item)

def cell_definition(my_dict):
    print('--',my_dict)
    selected_item = 'name1'
    changed_list =[]
    for key,value in my_dict.items():
        print('ячейка',key)
        for item in value:
            if item[0] == selected_item:
                changed_list.append(item)
    print(changed_list)

data = [['name1', '2024.11.01', 25, 1],['name1', '2024.10.01', 25, 2],['name2', '2024.01.21', 23, 3],['name3', '2024.12.21', 15, 3]]

def sorted_data(data):
    def date_key(item):
        return datetime.strptime(item[1], '%Y.%m.%d')
    sorted_list = sorted(data,key=date_key)
    print(sorted_list)


def ww():
    result = " \n"
    for item in data:
        result+=f'дата {item[1]} имя {item[0]}\n'
    print(result)
def insert_(data):
    for i in data:
        insert_data_to_cells(i)


if __name__ == '__main__':
    sorted_data(data)
    # sorted_list = sorted([[2, 'apple', 'Fiction'], [1, 'banana', 'Biography'], [4, 'grape', 'Science']],
    #                      key=lambda x: x)[1]
    # print(sorted_list)

    # data_dict = upload_data()
    # cell_definition(data_dict)
    # show_full(data_dict)
    # show_all(data_dict)
# create_cell(2)
# insert_data_to_cells(data)
# insert_(data)
# print(check_cell(1)[0][1])
# print(check_cell(data[3]))
# show_all()
# ww()