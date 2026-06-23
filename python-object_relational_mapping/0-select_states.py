#!/usr/bin/python3
'''Module Selects States From Table'''

import MySQLdb
from sys import argv


def select_states(username: str, password: str, database):
    '''Function to get States'''
    db = MySQLdb.connect(host='127.0.0.1', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    select_states(argv[1], argv[2], argv[3])
