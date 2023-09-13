from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Итегелова Виктория Олеговна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Виктория Итегелова, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html> 
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1> Первая лабораторная</h1>
        Текст про фласк

        <footer>
            &copy; Итегелова Виктория Олеговна, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html> 
"""


