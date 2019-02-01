# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 07:43:32 2019

@author: Sahithya
"""
from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def func():
    render_template('home.html')
    
if __name__=='__main__':
    app.run(debug=True)
    