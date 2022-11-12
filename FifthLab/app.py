from flask import Flask, render_template, request,redirect  # Импорт библиотек
import psycopg2
import hashlib
import os
# -----------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)  # Создание приложения
conn = psycopg2.connect(database="service_db",  # Подключение базы данных
                        user="postgres",
                        password="13579",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()  # Добавление курсора для обращения к базе данных
# -----------------------------------------------------------------------------------------------------------------------
@app.route('/login/', methods=['GET'])          # Декоратор
def index():
    return render_template('login.html')
# -----------------------------------------------------------------------------------------------------------------------
@app.route('/login/', methods=['POST', 'GET'])  # Декоратор
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            # Получение логина и пароля
            username = request.form.get('username')
            password = request.form.get('password')

            # Хеш. Проверка сохранненого в базе данных хеша с хешом, который создается при вводе нового пароля
            cursor.execute("SELECT * FROM service.users WHERE login=%s", [username])
            columns = cursor.fetchone()
            # Получение соли и хеша для пользователя. Так же проверка на наличие пользователя в базе данных.
            try:
                salt = columns[3]
                key = columns[4]
            except:
                return render_template("invalidPerson.html")
            # Создание хеша из введеного пароля пользователем и соли, которая использовалась для этого пользователя
            newkey = str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000))
            #Исключения при авторизации и получение информации с базы данных с помощью хеша
            if str(username) == '' or str(password) == '':
                return render_template('error.html')
            if (key == newkey):
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND hash=%s", (str(username), str(newkey)))
                records = list(cursor.fetchall())
                return render_template('account.html', full_name=records[0][1], login=username, password=password)
            else:
                return render_template("error.html")
        #Перенаправление на регистрацию
        elif request.form.get("registration"):
            return redirect("/registration/")
        return render_template('login.html')
# -----------------------------------------------------------------------------------------------------------------------
@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        #Получение информации при регистрации
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        #Проверка на пустые поля
        if str(name) == '' or str(login) == '' or str(password) == '':
            return render_template('error.html')
        #Проверка на занятый логин
        cursor.execute("SELECT login FROM service.users")
        usernames = list(cursor.fetchall())
        for i in range(len(usernames)):
            for j in range(len(usernames[i])):
                if usernames[i][j] == str(login):
                    return render_template('sameLogins.html')
        #Создание хеша и соли для пользователя
        salt = os.urandom(10)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        #Заполнение пользователя в базу данных
        cursor.execute('INSERT INTO service.users (full_name, login, salt, hash) VALUES(%s, %s, %s, %s);', (str(name), str(login), salt, str(key)))
        conn.commit()
        return redirect('/login/')
    return render_template('registration.html')
# -----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":  # Запуск приложения
    app.run()
# -----------------------------------------------------------------------------------------------------------------------