# coding: utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return 'Ring Fit Ranker!'


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()