from app.database import ps_connection as db

def add_user(email, password):
  query_str = f"INSERT INTO users (email, password) VALUES ('{email}', '{password}') RETURNING id, email"
  print('query_str: ', query_str)
  try:
    ps_cursor = db.cursor()
    ps_cursor.execute(query_str)
    result = ps_cursor.fetchone()
    print('result: ', result)
    return result
  except Exception as e:
    print(e)
    return None
