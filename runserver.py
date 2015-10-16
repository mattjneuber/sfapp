"""
Simple interactive data table
runserver.py - runs the local development server

Author: Matt Neuber
"""

from sfapp import app
from sfapp.database import init_db, db_session

init_db()
app.run(debug=True)
