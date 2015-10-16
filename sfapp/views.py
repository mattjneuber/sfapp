"""
Simple interactive data table
views.py - view functions

Author: Matt Neuber
"""

from sfapp import app
from sfapp.database import db_session
from sfapp.models import Person
from flask import render_template, request
import json
import datetime

@app.route('/')
def index():
    people = Person.query.all()
    return render_template('index.html', people=people)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        data = request.get_json()
        # the incoming dictionary contains the fields: id, field, value
        # id: row ID for the database entry we're editing
        # field: field in the record we're interested in updating
        # value: the new value to assign to the field
        record = Person.query.filter(Person.id == data["id"]).first()
        if record:
            # in the case of the date of birth field, we must first
            # convert to a Python date object
            if data["field"] == "dob":
                data["value"] = datetime.datetime.strptime(data["value"], "%Y-%m-%d").date()
            setattr(record, data["field"], data["value"])
            db_session.commit()
    return "Nothing here!"

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        data = request.get_json()
        record = Person.query.filter(Person.id == data["id"]).first()
        if record:
            db_session.delete(record)
            db_session.commit()
            return json.dumps({"status": "OK"})
    return "Nothing here!"

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        dob = datetime.datetime.strptime(data["dob"], "%Y-%m-%d").date()
        zip_code = data["zip_code"]
        print first_name, last_name, dob, zip_code
        person = Person(first_name, last_name, dob, zip_code)
        db_session.add(person)
        db_session.commit()
        return json.dumps({"status": "OK"})
    return "Nothing here!"
