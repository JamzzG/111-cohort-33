#!/usr/bin/env python3
# -*- coding ucf8 -*-
"""Sample hellow world Flask app"""

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list

@app.route("/aboutme", methods=["GET"])
def about_me():
    about= {
        "first_name": "James",
        "last_name": "Grantham",
        "hobby": "Skateboarding"
    }
    return jsonify(about)
