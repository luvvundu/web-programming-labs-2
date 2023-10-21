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

    if __name__ == "__main__":
        app.run()