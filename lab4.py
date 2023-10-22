from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    error_username = None
    error_password = None

    if request.method == 'GET': 
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html')
    
    if not username:
        error_username = "Не введен логин"

    if not password:
        error_password = "Не введен пароль"
    
    error = 'Неверные логин и/или пароль'
    return render_template('login.html', error=error, error_username=error_username, error_password=error_password)


@lab4.route("/lab4/fridge", methods=["GET", "POST"])
def fridge():
    if request.method == "POST":
        temperature = request.form.get("temperature")

        if not temperature:
            error = "Ошибка: не задана температура"
            return render_template("fridge.html", error=error)

        temperature = int(temperature)
        if temperature < -12:
            error = "Не удалось установить температуру — слишком низкое значение"
        elif temperature > -1:
            error = "Не удалось установить температуру — слишком высокое значение"
        else:
            error = None

        return render_template("fridge.html", temperature=temperature, error=error)

    return render_template("fridge.html")


@lab4.route("/lab4/zerno", methods=["GET", "POST"])
def zerno():
    if request.method == "POST":
        zerno = request.form.get("zerno")
        weight = request.form.get("weight")

        if not weight:
            error = "Ошибка: не введён вес"
            return render_template("zerno.html", error=error)

        try:
            weight = float(weight)
            if weight <= 0:
                error = "Ошибка: неверное значение веса"
                return render_template("zerno.html", error=error)
        except ValueError:
            error = "Ошибка: неверное значение веса"
            return render_template("zerno.html", error=error)

        prices = {
            "ячмень": 12000,
            "овёс": 8500,
            "пшеница": 8700,
            "рожь": 14000
        }

        if weight > 500:
            error = "Извините, такого объёма сейчас нет в наличии"
            return render_template("zerno.html", error=error)

        order_total = prices[zerno] * weight
        discount = weight > 50

        return render_template("zerno_success.html", zerno=zerno, weight=weight, order_total=order_total, discount=discount)

    return render_template("zerno.html")


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    headers = {
        'Set-Cookie': 'color=' + color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers
    
