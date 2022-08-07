"""
Function create database
"""
import os.path
import sqlite3
import create_barcode

def open_db():
    """
    Function opens database
    :return: connection, cursor
    """
    con = sqlite3.connect('db/company.db')
    cur = con.cursor()

    return con, cur

def add_workers(con, cur, data=None):
    """
    Function inserts new row of database
    :param data: list with tuple: one row one column

    """
    # add new worker
    if not data:
        data = []

        while True:
            next_item = input("Add worker\nPress q to exit, to continue press enter ")
            if next_item == 'q':
                break
            name = input("name: ")
            address = input("address: ")
            salary = float(input("salary: "))
            ean_code = input("ean code: ")
            if not ean_code:
                ean_code = create_barcode.create_ean13('barcode/company/worker')
            print(name, address, salary, ean_code)
            data.append((name, address, salary,ean_code))

    sql = f"INSERT INTO worker VALUES(?,?,?,?)"
    cur.executemany(sql, data)
    con.commit()

def automatic_add_worker(con, cur, n=5):
    """
    Function inserts new random row of database
    :param n: amout of row
    :return: cursor
    """

    from faker import Faker
    from random import randint
    fake = Faker('pl')
    data = []
    print("Add random data: ")
    for i in range(n):
        name = fake.name()
        address = fake.address()
        salary = float(randint(20,1000))
        ean_code = create_barcode.create_ean13('barcode/company/worker')
        data.append((name,address,salary,ean_code))
        print(name,address,salary,ean_code)

    sql = f"INSERT INTO worker VALUES(?,?,?,?)"
    cur.executemany(sql, data)
    con.commit()
    return cur

def all_data(con, cur):
    """
    Print all datebase

    """
    print('*'*50)
    for row in cur.execute('SELECT rowid, name, address, salary, code FROM worker ORDER BY rowid'):
        print(row)

    print('*'*50)

def search(con, cur, name):
    """
    The function searches with database
    :param name: key
    """
    sql = f"SELECT * FROM worker WHERE name LIKE '%{name}%'"
    s = cur.execute(sql)
    for i in cur.execute(sql):
        print(i)
    if not s:   print("Not find. ")

def is_database():
    """
    Check if database exist.
    :return:
    """
    if not os.path.exists('db/company.db'):
        #create db
        con, cur = open_db()
        # Create table -> worker
        cur.execute(
            """
            CREATE TABLE worker
            (name TEXT, address TEXT, salary REAL, code TEXT NOT NULL UNIQUE)
            """
        )
        con.commit()
    else:
        #open db
        con, cur = open_db()
    return con, cur

def main():
    """
    The function create, add random row , print and close database
    :return:
    """
    con, cur = is_database()
    automatic_add_worker(con, cur, 10)
    for row in cur.execute('SELECT * FROM worker ORDER BY rowid'):
        print(row)
    con.close()


if __name__ == '__main__':
    main()