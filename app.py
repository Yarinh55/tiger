#!/usr/bin/env python3
from flask import Flask, render_template
import mysql.connector

mydatabase = mysql.connector.connect(
    host = 'localhost', user = 'root',
    passwd = 'LoginPass@@11223344', database = 'tiger')

mycursor = mydatabase.cursor()

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')

@app.route('/messages_view')
def messages_view():
    return render_template('/messages_view.html')

@app.route('/messages_view')
def messages_view():
	mycursor.execute("SELECT * FROM tiger.messages")
	data = mycursor.fetchall()
	return render_template('messages_view.html', data=data)
	

if __name__ == '__main__':
    app.run(host='0.0.0.0')
