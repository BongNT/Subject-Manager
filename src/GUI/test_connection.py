import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None

    conn = mysql.connector.connect(host='localhost', user='root', port='3307', database='test')
    if conn.is_connected():
        print('Connected to MySQL database')

    cur = conn.cursor()

    try:
        dbs = cur.execute("show databases")
    except:
        conn.rollback()
    for x in cur:
        print(x)

    conn.close()


if __name__ == '__main__':
    connect()
