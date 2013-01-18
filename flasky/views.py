from flasky import app
from flask import url_for, render_template, request, jsonify

with app.test_request_context():
    url_for('static', filename='js/jquery-1.9.0.min.js')
    url_for('static', filename='css/styles.css')

@app.route('/', methods=['GET',])
def index():
    c = {}
    return render_template('index.html', **c)

@app.route('/page', methods=['GET',])
def page():
    c = {}
    return render_template('page.html', **c)