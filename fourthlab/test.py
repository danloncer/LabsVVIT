import psycopg2
import hashlib
import os

conn = psycopg2.connect(database="service_db",    #Подключение базы данных
                        user="postgres",
                        password="13579",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()                            #Добавление курсора для обращения к базе данных

login = 'alina'
password = '951951'

salt = os.urandom(10)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
cursor.execute('UPDATE service.users SET salt=%s, hash=%s WHERE login=%s', (salt, str(key), str(login)))
conn.commit()