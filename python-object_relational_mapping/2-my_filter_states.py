#!/usr/bin/python3
'''Search states by name'''

import MySQLdb
from sys import argv


def search_states(username: str, password: str, database, state: str):
    '''Function to search States'''
    db = MySQLdb.connect(host='127.0.0.1', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC" % (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    search_states(argv[1], argv[2], argv[3], argv[4])
