from flask import Blueprint, render_template, request, make_response
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
        return render_template('success.html', username=username)
    
    if username == '':
        error_username = "Не введен логин"

    if password == '':
        error_password = "Не введен пароль"
    
    error = 'Неверные логин и/или пароль'
    return render_template('login.html', error = error, error_username = error_username,
                            error_password = error_password)

@lab4.route("/lab4/fridge", methods=["GET", "POST"])
def fridge():
    if request.method == "POST":
        temperature = request.form.get("temperature")

        if not temperature:
            error = "Ошибка: не задана температура"
            return render_template("fridge.html", temperature=None, error=error)

        temperature = int(temperature)
        if temperature < -12:
            error = "Не удалось установить температуру — слишком низкое значение"
        elif temperature > -1:
            error = "Не удалось установить температуру — слишком высокое значение"
        else:
            error = None

        return render_template("fridge.html", temperature=temperature, error=error)

    return render_template("fridge.html", temperature=None)

@lab4.route("/lab4/zerno", methods=["GET", "POST"])
def zerno():
    if request.method == "POST":
        zerno = request.form.get("zerno")
        weight = request.form.get("weight")

        prices = {
            "ячмень": 12000,
            "овёс": 8500,
            "пшеница": 8700,
            "рожь": 14000
        }

        if not zerno:
            error = "Ошибка: не верно выбрано зерно."
            return render_template("zerno.html", error=error)
        
        if not weight or int(weight) <= 0:
            error = "Ошибка: не верно указан вес."
            return render_template("zerno.html", error=error)

        weight = int(weight)

        if weight > 500:
            error = "Извините, такого объёма сейчас нет в наличии.  "
            return render_template("zerno.html", error=error)

        discount = False

        if (weight >= 50):
            order_total = (prices[zerno] * weight) * 0.9
            discount = True
        else:
            order_total = prices[zerno] * weight

        return render_template("zerno_success.html", zerno=zerno, weight=weight, order_total=order_total, discount=discount)

    return render_template("zerno.html")

    
    
@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color_text = request.form.get('color_text')
    color_bg = request.form.get('color_bg')
    font_size = request.form.get('font_size')

    response = make_response('', 303)
    
    response.headers['Location'] = 'cookies'
    
    response.set_cookie('color', color_text)
    response.set_cookie('bgColor', color_bg)
    
    if (not font_size):
        return response

    response.set_cookie('fontSize', font_size)
    
    return response
