# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:48:52 2019

@author: Sahithya
"""

"""
 flask is the framework here, while Flask is a Python class datatype. In other words, 
 Flask  is the prototype used to create instances of web application or web applications
 
"""

from flask import Flask
app = Flask(__name__) #create an instance of an app 

@app.route("/hi")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True) #app will being run if we run from app.py.
    
#build simple restful api with flask and SQLite that have capabilities to create, read, update, and delete data from database.
    
    