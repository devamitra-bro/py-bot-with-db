import psycopg2

def execute(sql: str):
    conn = psycopg2.connect(dbname='am', user='postgres', password='password', host='localhost') # todo move to some props file
    cursor = conn.cursor()
    res = []
    try:
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
    except Exception as error:
        print('execute sql err -> ', error)
        cursor.close()
        conn.close()

    cursor.close()
    conn.close()
    return res


res = execute(
    """
    select * from base_user limit 2
    """
)

print(res)