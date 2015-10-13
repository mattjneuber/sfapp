from sfapp import app
from sfapp.database import db_session
from sfapp.models import Person
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
