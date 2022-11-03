import os
import json
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
directory = {'Ian':'0000','Chris':'1111','Wendy':'2222'}

app = Flask(__name__)
@app.route("/Hello", methods=['GET'])
def returnHello():
    if request.method == 'GET':
        print("Executing Hello")
        return "Hello world"

@app.route("/Directory", methods=['GET'])
def returnDir():
    if request.method == 'GET':
        print("getting directory.")
        return json.dumps(directory);


# Exercise 1:
@app.route("/Length", methods=['GET'])
def dirLength():
    if request.method == 'GET':
        print("getting length")
        return str(len(directory))

# ----------------------------------------------------------------
# You could put this into the /Directory route to be better
# but this seperates the code for simplicity of the session.
@app.route("/AddContact", methods=['POST'])
def addContact():
    print('processing Data')
    message ='already there'
    if request.method == 'POST':
        name = request.form['name']
        num = request.form['num']
        if not(name in directory):
            message = 'ok'
            directory[name] =  num
        print(directory)
    return message

# this is the route for ex2
@app.route("/DeleteContact", methods=['DELETE'])
def delContact():
    print('processing Data')
    if request.method == 'DELETE':
        name = request.form['name']
        if (name in directory):
            del directory[name]
        else:
            return 'not there'
        print(directory)
    return name + " is delete"


@app.route("/More", methods=['GET'])
def more():
    if request.method == 'GET':
        return "<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>  hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>hi<br>"


if __name__ == "__main__":
    app.run(debug=True)
