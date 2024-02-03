from flask import Flask, render_template, request
from flaskwebgui import FlaskUI

import random as random

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

def randRoll(roll):
    return random.randrange(1, roll + 1, 1)

def main():
    while(1):
        inVal = input('Enter command:')
        if (inVal == "stop"):
            break
        elif(inVal == "1"):
            print("1")
        else:
            print(randRoll(int(inVal)))
    return

if(__name__ == "__main__"):
    # main()
    # FlaskUI(app, width=500, height=500).run()
    app.run()