from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return jsonify(message='Hallo Welt!!'), 200


@app.route('/not_found')
def not_found():
    return jsonify(message='not found'), 404


@app.route("/parameters")
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='leider ' + name), 401
    else:
        return jsonify(message='Willkommen ' + name)


@app.route('/url_vars/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message='leider ' + name), 401
    else:
        return jsonify(message='Willkommen ' + name)


if __name__ == '__main__':
    app.run()
