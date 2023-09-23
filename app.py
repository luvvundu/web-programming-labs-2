from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <h1>НГТУ, ФБ, Лабораторные работы</h1>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <footer style='margin-top:20px;'>
            &copy; Итегелова Виктория Олеговна, ФБИ-13, 3 курс, 2023
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
        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        
        <footer style='margin-top:20px;'>
            &copy; Итегелова Виктория Олеговна, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html> 
"""

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href=''' + url_for('static', filename='lab1.css') + ''' />
    </head>
<html>
    <body>
        <h1>Дуб</h1>
        <img src='''+ url_for('static', filename='oak.jpg') + '''>
    </body>
</html>
'''