#!/usr/bin/python3
"""Lists all cities with their states"""

import MySQLdb
from sys import argv


def list_cities(username, password, database):
    """Function that lists cities by state"""
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # ONE execute() only + JOIN states and cities
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
