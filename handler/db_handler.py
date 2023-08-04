import sqlite3
from hash_passw import *


def login(login, passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()
    check_passw = str(check_hash_key(passw))

    if value != [] and value[0][2] == check_passw:
        signal.emit("Успешная авторизация")
    else:
        signal.emit("Не успешная авторизация")

    cur.close()
    con.close()


def register(login, passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit("Данное имя занято")
    elif value == []:
        password = hpassw(passw)
        cur.execute(f'INSERT INTO users (name, password) VALUES ("{login}", "{password}")')
        signal.emit("Вы зарегистрировалсь!")
        con.commit()

    cur.close()
    con.close()
