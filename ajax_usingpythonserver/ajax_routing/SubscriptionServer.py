import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
names = []

app = Flask(__name__)



@app.route("/AddContact", methods=['POST'])
def addContact():
    print('processing Data')
    message ='already there'
    if request.method == 'POST':
        name = request.form['name']
        names.append(name)
    return redirect('/static/thankyou.html')


@app.route("/customer", methods=['GET'])
def getCustomer():
    # Ex3: todo

@app.route("/More", methods=['GET'])
def more():
    if request.method == 'GET':
        return more;

more = "more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>more<br>";

if __name__ == "__main__":
    app.run(debug=True)
