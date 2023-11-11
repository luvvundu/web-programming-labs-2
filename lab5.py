from flask import Blueprint, redirect, render_template, request
import psycopg2

lab5 = Blueprint('/lab5', __name__)

@lab5.route('/lab5')
def main():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base',
        user='ivictoria_knowledge_base',
        password='12345'
    )

    cur = conn.cursor()

    cur.execute('SELECT * FROM users;')

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return "go to console"

