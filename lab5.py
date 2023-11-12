from flask import Blueprint, redirect, render_template, request
import psycopg2

lab5 = Blueprint('/lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
         host='127.0.0.1',
        database='knowledge_base',
        user='ivictoria_knowledge_base',
        password='12345'
    )

    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5')
def main():
    visibleUser = 'Anon'

    return render_template('lab5.html', username = visibleUser)

@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base',
        user='ivictoria_knowledge_base',
        password='12345'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')

    result = cur.fetchall()

    return(result)