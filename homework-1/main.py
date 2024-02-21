"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from config import customers_path, employees_path, orders_path
import csv


def read_csv_file(file_path) -> list:
    """ Чтение CSV  файла
    param file_path: Файл CSV
    return: Данные CSV файла
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        count = 0
        data_list = []
        for row in file_reader:
            if count == 0:
                pass
            else:
                data_list.append(row)
            count += 1

    return data_list


def create_symbols(file_name: list) -> str:
    """ Выводит символы %s в зависимости от длинны списка
    params file_name: Данные CSV файла
    return: Символы
    """
    symbols = []
    for item in range(len(file_name[1])):
        symbols.append('%s')
    symbols = ', '.join(symbols)

    return symbols


def writing_to_the_database(file_name: list, name_database: str) -> None:
    """ Запись данных из csv файлов в таблицы
    param file_name: Данные csv файла
    param name_database: Название таблицы в базе данных
    """
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty') as conn:
        with conn.cursor() as cur:
            cur.executemany(f"INSERT INTO {name_database} VALUES ({create_symbols(file_name)})", file_name)
            cur.execute("SELECT * FROM customers")

            # rows = cur.fetchall()
            # for row in rows:
            #     print(row)

    conn.close()


# Словарь с ключами csv файлов, а его значение название таблицы
dict_csv_file = {customers_path: 'customers', employees_path: 'employees', orders_path: 'orders'}

for key, value in dict_csv_file.items():
    writing_to_the_database(read_csv_file(key), value)
