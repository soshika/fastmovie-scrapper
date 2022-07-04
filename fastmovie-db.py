import psycopg2

conn = psycopg2.connect(
   database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
)