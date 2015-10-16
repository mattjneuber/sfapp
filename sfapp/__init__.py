"""
Simple interactive data table
package - main package driver for Flask

Author: Matt Neuber
"""

from flask import Flask
from sfapp.database import db_session

app = Flask(__name__)

import sfapp.views

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
