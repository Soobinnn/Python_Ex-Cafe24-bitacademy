import psycopg2
import config

try:
    conn = psycopg2.connect(
        user='webdb',
        password='webdb',
        host='192.168.1.118',
        port='5432',
        database='webdb')

    cursor = conn.cursor()
    cursor.execute('select version()')
    record = cursor.fetchone()


except Exception as e:
    print(f'error:{e}')
finally:
    'conn' and conn.close()
