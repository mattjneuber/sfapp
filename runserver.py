from sfapp import app
from sfapp.database import init_db

init_db()
app.run(debug=True)
