from app.database import ps_connection as db

def add_user(email, password):
  query_str = f"INSERT INTO users (email, password) VALUES ('{email}', '{password}') RETURNING id, email"
  try:
    ps_cursor = db.cursor()
    ps_cursor.execute(query_str)
    result = ps_cursor.fetchone()
    print('result: ', result)
    return result
  except Exception as e:
    print(e)
    return None

def get_user(email):
  query_str = f"SELECT * FROM users WHERE email = '{email}'"
  try:
    ps_cursor = db.cursor()
    ps_cursor.execute(query_str)
    result = ps_cursor.fetchone()
    print('result in dbHelpers: ', result)
    return result
  except Exception as e:
    print(e)
    return None
