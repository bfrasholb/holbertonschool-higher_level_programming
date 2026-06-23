#!/usr/bin/python3
"""Filter states by name"""

import MySQLdb
from sys import argv


def filter_states():
    """Function to filter States"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv, passwd=argv, db=argv)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(argv))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
