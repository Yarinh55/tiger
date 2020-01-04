#!/usr/bin/env python3
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="LoginPass@@11223344",
    database="tiger"
)
cursor = connection.cursor()


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


@app.route('/messages_view')
def messages_view():
    mySql_insert_query = """INSERT INTO tiger.users (username,password,create_date)
    VALUES('YarinAndMor','RandomPass123545','2020-01-01 10:09:10')"""
    cursor.execute(mySql_insert_query)
    connection.commit()
    mySql_insert_query2 = """INSERT INTO tiger.messages ((username,create_date,content)
    VALUES('YarinAndMor','2020-01-01 10:10:10',
    'This is my first message,Hello world')"""
    cursor.execute(mySql_insert_query2)
    connection.commit()
    cursor.execute("SELECT * FROM tiger.messages")
    data = cursor.fetchall()
    cursor.close()
    return render_template('messages_view.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
