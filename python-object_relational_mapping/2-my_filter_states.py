#!/usr/bin/python3
"""Filter states by name"""


import MySQLdb
from sys import argv


def filter_states(username, password, database, state):
    """Function to filter States"""
    db = MySQLdb.connect(host='127.0.0.1', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC", (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(argv[1], argv[2], argv[3], argv[4])
