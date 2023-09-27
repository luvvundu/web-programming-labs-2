from flask import Flask, redirect, url_for, render_template
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

        <h3>Меню:</h3>
        <ol>
            <li>
            <a href='/lab1'>Первая лабораторная работа</a>
            </li>
            <li>
            <a href='/lab2'>Вторая лабораторная работа</a>
            </li>
        </ol>

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
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных:
        </header>

        <h1>Первая лабораторная</h1>
        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>

        <ol>
          <li><a href="/lab1/oak">Дуб</a></li>
          <li><a href="/lab1/student">Студент</a></li>
          <li><a href="/lab1/python">Python</a></li>
          <li><a href="/lab1/winx">Winx</a></li>
        </ol> 

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
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="'''+ url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
   <head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>

<html>
    <body>
        <h1>Итегелова Виктория Олеговна</h1>
        <img src="''' + url_for('static', filename='ngtu.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
<html>
    <body>
        <h1>Python</h1>
        <p>
        Первая версия Python была разработана в 1991 году программистом 
        из Нидерландов Гвидо ван Россумом. В настоящее время выходят новые версии языка, которые 
        расширяют его возможности, а сам он занимает верхние строчки рейтингов языков программирования. 
        Python применяется во многих сферах: веб-разработка, анализ данных и машинное обучение и др.
        </p>

        <p>
        Главное достоинство Python — простота синтаксиса и команд, а также большое количество библиотек, 
        которые содержат уже написанный программный код для решения широкого спектра задач. Python даже применяют 
        в своих исследованиях и разработках специалисты, чьи профессии напрямую не связаны с программированием. 
        Один из самых частых примеров — применение Python для анализа большого количества данных и нахождения корреляции между ними.
        </p>

        <p>
        Все языки программирования можно условно разделить на две большие группы: компилируемые и 
        интерпретируемые. Программы, написанные на компилируемых языках программирования, преобразуются 
        (компилируются) в машинный код и становятся исполняемыми (например, в операционной системе Windows 
        это чаще всего будет файл с расширением .exe). Программы, написанные на интерпретируемых языках 
        (в их числе и Python), не компилируются, и для их запуска требуется специальная программа — интерпретатор.
        </p>

        <img src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/winx')
def winx():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
<html>
    <body>
    <h1>Winx</h1>

    <p>
    Клуб Винкс» (англ. Winx Club) — фантастический мультсериал производства Rainbow S.r.l., 
    созданный по замыслу итальянского аниматора Иджинио Страффи. Премьера состоялась 28 января 2004 года в Италии на 
    канале Rai 2. Действие происходит во вселенной, наполненной волшебством, вымышленными планетами и мифическими созданиями.
    </p>

    <p>
    Действие происходит во вселенной, наполненной волшебством, вымышленными планетами и мифическими созданиями. 
    В основе сюжетной линии мультсериала лежит история юной 
    девушки Блум, её поиски правды о своём прошлом и о том, что случилось с её родной планетой и настоящими родителями. 
    </p>

    <p>
    Узнав, что у неё есть волшебные силы, Блум поступила в школу 
    для фей и вместе со своими сокурсницами основала команду под названием «Клуб Винкс», чтобы вместе сражаться со злом..
    </p>

    <img src="''' + url_for('static', filename='winx.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Victoria Itegelova'
    group = 'ФБИ-13'
    number_lab = 'Лабораторная работа 2'
    number_kurs = '3 курс'
    fruits = [
        {'name' : 'бананы', 'price' : 150},
        {'name' : 'мандарины', 'price' : 200}, 
        {'name' : 'яблоки', 'price' : 300},
        ]
    
    books = [
        {'book' : 'Мастер и Маргарита', 'author' : 'Михаил Булгаков', 'zhanr' : 'Любовный роман', 'str' : 480},
        {'book' : 'Сила подсознания', 'author' : 'Джо Диспенза', 'zhanr' : 'Зарубежная психология', 'str' : 550},
        {'book' : 'Ни сы', 'author' : 'Джен Синсеро', 'zhanr' : 'Зарубежная психология', 'str' : 220},
        {'book' : 'К себе нежно', 'author' : 'Ольга Примаченко', 'zhanr' : 'Психология', 'str' : 380},
        {'book' : 'Отцы и дети', 'author' : 'иван Тургенев', 'zhanr' : 'Роман', 'str' : 280},
        {'book' : 'Маленькие женщины', 'author' : 'Луиза Мэй Олкотт', 'zhanr' : 'Драма, мелодрама', 'str' : 200},
        {'book' : 'Харизма', 'author' : 'Оливия Кабейн', 'zhanr' : 'Психология', 'str' : 240},
        {'book' : 'Гранатовый браслет', 'author' : 'Александр Куприн', 'zhanr' : 'Повесть', 'str' : 390},
        {'book' : 'Не тупи', 'author' : 'Джон Синсеро', 'zhanr' : 'Зарубежная психология', 'str' : 70},
        {'book' : 'Люби', 'author' : 'Камал Равикант', 'zhanr' : 'Зарубежная психология', 'str' : 80},
        {'book' : '5 языков любви', 'author' : 'Гэри  Чепмен', 'zhanr' : 'Практическая психология', 'str' : 130},
    ]

    return render_template('example.html', 
                            number_lab = number_lab,
                              name=name, group = group, 
                              number_kurs = number_kurs, 
                              fruits = fruits,
                              books = books,
                            )

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/cartoons')
def cartoons():
    return render_template('cartoons.html')
