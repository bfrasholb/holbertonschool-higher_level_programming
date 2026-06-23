#!/usr/bin/python3
'''Filter states by name'''

import MySQLdb
from sys import argv


def filter_states(username: str, password: str, database):
    '''Function to get States'''
    db = MySQLdb.connect(host='127.0.0.1', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(argv[1], argv[2], argv[3])
