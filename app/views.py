from app import app
from flask import request
from operator import itemgetter
import app.database.dbHelpers as db

@app.route('/signup', methods=['POST'])
def signup():
  data = request.get_json()
  email, password = itemgetter('email', 'password')(data)

  return "signup"