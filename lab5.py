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
    conn = dbConnect()

    cur = conn.cursor()

    cur.execute('SELECT * FROM users;')

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    dbClose(cur, conn)
    
    return "go to console"

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