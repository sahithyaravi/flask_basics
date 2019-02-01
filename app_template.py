# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 07:43:32 2019

@author: Sahithya
"""
    
from flask import Flask,render_template
app = Flask(__name__) #create an instance of an app 

@app.route("/temp")
def hello():
    return render_template('home.html')

@app.route("/temp/about")
def abt():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #app will being run if we run from app.py.
    
#build simple restful api with flask and SQLite that have capabilities to create, read, update, and delete data from database.
    
    