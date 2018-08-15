#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
   return "Ceci est la page d'accueil."

@app.route('/hello/<phrase>')
def hello(phrase):
   return "hello "+phrase

@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)

@app.route('/contact', methods=['POST'])
def postContact():
    mail = request.get_json()['mail']
    tel = request.get_json()['tel']
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)
