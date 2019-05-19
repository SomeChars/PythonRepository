import flask
from flask import Flask, request
import math
import random

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/check_it/<int:number>')
@app.route('/check_it')
def check_it(number=random.randint(0, 100)):
    if number is None:
        return "went wrong..."
    if number == 2 or number == 1:
        return "I don't think "+str(number)+" is primal"
    for i in range(2, 1 + math.ceil(math.sqrt(number))):
        if number % i == 0:
            return "I don't think " + str(number) + " is primal"
    return "Hmm... Maybe "+str(number)+" is a primal number"


@app.route('/')
def root():
    return flask.render_template('index.html')


@app.route('/number', methods=['GET', 'POST'])
def numerology():
    if request.method == 'POST':
        number_param = int(request.form.get('number'))
        return flask.render_template(
            'number.html',
            number=number_param,
            method=request.method,
            res=check_it(number_param)
        )

    return flask.render_template(
        'number.html',
        number=42,
        method=request.method,
        res=check_it(42)
    )


if __name__ == '__main__':
   app.run(debug=True)