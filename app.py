from flask import Flask
from lab1 import lab1 
from lab2 import lab2 
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5 

app = Flask(__name__)


app.secret_key = "12345"
user_db = 'ivictoria_knowledge_base'
host_ip = '127.0.0.1'
host_port = '5432'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

