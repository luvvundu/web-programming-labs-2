from flask import Blueprint, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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
        {'book' : 'Отцы и дети', 'author' : 'Иван Тургенев', 'zhanr' : 'Роман', 'str' : 280},
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


@lab2.route('/lab2/')
def lab_2():
    return render_template('lab2.html')


@lab2.route('/lab2/cartoons')
def cartoons():
    return render_template('cartoons.html')