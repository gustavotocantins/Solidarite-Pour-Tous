from flask import Flask, render_template, url_for, request, redirect
from os import chdir
import os

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opportunites')
def oportunidades():
    return render_template('oportunidades.html')

if __name__ == '__main__':
    app.run()