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

        <h2>1. Первая лабораторная</h2>
        <a href="/lab1">Перейти на лабораторную 1</a>

        <footer>
            &copy; Итегелова Виктория Олеговна, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html> 
"""


