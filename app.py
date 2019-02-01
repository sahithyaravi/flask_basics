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

@app.route('/') #the function below is mapped to the home url (localhost:5000)
def hello():
    return "Hello there!"


#Python assigns the name "__main__" to the script when the script is executed.
if __name__=='__main__': # this condition is satisfied when we run this script
   app.run(debug=True)