from flask import Flask, render_template, request #Импорт библиотек
import psycopg2
import hashlib

app = Flask(__name__)                             #Создание приложения
conn = psycopg2.connect(database="service_db",    #Подключение базы данных
                        user="postgres",
                        password="13579",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()                            #Добавление курсора для обращения к базе данных

@app.route("/login/", methods=['GET'])            #Первый декоратор
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])           #Второй декоратор
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    #Хеш. Проверка сохранненого в базе данных хеша с хешом, который создается при вводе нового пароля
    cursor.execute("SELECT * FROM service.users WHERE login=%s", [username])
    columns = cursor.fetchone()
    #Получение соли и хеша для пользователя
    salt = columns[3]
    key = columns[4]
    #Создание хеша из введеного пароля пользователем и соли, которая использовалась для этого пользователя
    newkey = str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt , 100000))

    if str(username) == '' or str(password) == '':      #Исключение (Проверка полей на пустоту)
        return render_template('error.html')            #Перенаправляет на страницу с ошибкой
    try:                                                #Исключение (Проверка наличия пользователя в базе данных
        if (key == newkey): #Проверка хеша из базы данных с новым хешем
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND hash=%s", (str(username), str(newkey)))
            records = list(cursor.fetchall())
            return render_template('account.html', full_name=records[0][1], login=username, password=password)
    except:
        return render_template('invalidPerson.html')    #Перенаправляет на страницу с ошибкой

if __name__ == "__main__":                  #Запуск приложения
    app.run()
