import psycopg2


def test_insert():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("insert into pet values('베리','임수빈','cat','m', '2018-1-13', null)")
    except Exception as e:
        print('error: %s' %e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_select():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("select * from pet")
        records = cursor.fetchall()
    except Exception as e:
        print('error: %s' %e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())

def test_delete():
    try:


def main():
    test_insert()
    # test_select()
    print('===============================')
    # test_delete()
    # test_select()
    print('===============================')
    # test_update()
    # test_select()





__name__ == '__main__' and main()
