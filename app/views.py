from app import app
from app.database import postgreSQL_pool as db

@app.route('/')
def root():
  return "root"

@app.route('/signup')
def signup():
  return "signup"