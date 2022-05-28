import psycopg2
import os
from psycopg2 import pool

try:
  postgreSQL_pool = pool.SimpleConnectionPool(
    1,
    100,
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    database=os.environ.get('DB_DATABASE'),
  )

  if (postgreSQL_pool) :
    print("Connection pool created successfully")

except (Exception, psycopg2.DatabaseError) as error:
  print("Error while connecting to PostgresQL", error)

finally:
  if postgreSQL_pool:
    postgreSQL_pool.closeall
  print("PostgreSQL connection pool is closed")