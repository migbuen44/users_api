import numbers
from dotenv import load_dotenv
load_dotenv()

import app.database.dbHelpers as dbHelper
from app.database import ps_connection as db

# TEST VARIABLES

test_email = "test@gmail.com"
test_password = "password"
delete_query_str = f"DELETE FROM users WHERE email='{test_email}'"

# TEST SETUP

ps_cursor = db.cursor()
ps_cursor.execute(delete_query_str)

# TESTS

def test_add_user():
  result = dbHelper.add_user(test_email, test_password)
  # print('result: ', result)
  result_id, result_email = result
  assert type(result_id) is int
  assert result_email == test_email

def test_get_user():
  result = dbHelper.get_user(test_email)
  result_id, result_email, result_password = result
  assert type(result_id) is int
  assert result_email == test_email
  assert result_password == test_password

# TEST TEARDOWN

ps_cursor = db.cursor()
ps_cursor.execute(delete_query_str)

print("Hello from dbHellperTests")
from dotenv import load_dotenv

load_dotenv()

# from app.database import ps_connection as db
from app import app






