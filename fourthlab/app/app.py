from flask import Flask, render_template, request #Импорт библиотек
import psycopg2

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

    if str(username) == '' or str(password) == '':      #Исключение (Проверка полей на пустоту)
        return render_template('error.html')            #Перенаправляет на страницу с ошибкой
    try:                                                #Исключение (Проверка наличия пользователя в базе данных
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        return render_template('account.html', full_name=records[0][1], login=username, password=password)
    except:
        return render_template('invalidPerson.html')    #Перенаправляет на страницу с ошибкой

if __name__ == "__main__":                  #Запуск приложения
    app.run()
