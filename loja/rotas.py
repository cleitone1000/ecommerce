from flask import render_template, session, request, url_for

from loja import app, db


@app.route('/')


def home():
    return "Hello World!"