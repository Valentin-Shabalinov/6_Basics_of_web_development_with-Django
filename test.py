import psycopg2

conn = psycopg2.connect(dbname='test_db', user='root', password='root', host='127.0.0.1', port=5433)
cursor=conn.cursor()


cursor.execute('SELECT version()')
print(cursor.fetchone())
cursor.close() # закрываем курсор
conn.close() # закрываем соединение