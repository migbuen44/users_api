from app import app
from flask import request, Response
from operator import itemgetter
import app.database.dbHelpers as db

json = 'application/JSON'

@app.route('/signup', methods=['POST'])
def signup():
  data = request.get_json()
  email, password = itemgetter('email', 'password')(data)
  result = db.add_user(email, password)
  if not result:
    return Response(status=409)
  result_id, result_email = result
  response_body = {
    'id': result_id,
    'email': result_email,
  }

  return response_body

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email, password = itemgetter('email', 'password')(data)
  result = db.get_user(email)
  print('result in views: ', result)
  return 'login'