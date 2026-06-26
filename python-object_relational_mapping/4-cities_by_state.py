#!/usr/bin/python3
"""Lists all cities with their states"""

import MySQLdb
from sys import argv


def list_cities(username, password, database):
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    rows = cur.fetchall()

    for row in rows:
        print("{} {}".format(row[0], row[1]))

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
