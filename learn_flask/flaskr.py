#!/usr/bin/env python
# coding=utf-8
import pymysql
from flask import Flask, render_template, request,flash

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-'
USERNAME = 'admin'
PASSWORD = 'default'

conn = pymysql.connect()
cursor = conn.cursor()

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash('You were login')
    return render_template('homePage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', name=request.form['name'], password=request.form['password'])

if __name__ == '__main__':
    app.run()
