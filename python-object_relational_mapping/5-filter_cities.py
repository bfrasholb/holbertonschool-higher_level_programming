#!/usr/bin/python3
"""Lists all cities of a given state"""

import MySQLdb
from sys import argv


def filter_cities(username, password, database, state_name):
    """Function that lists cities by state name safely"""
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    rows = cur.fetchall()

    if rows:
        print(", ".join(city[0] for city in rows))

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 5:
        filter_cities(argv[1], argv[2], argv[3], argv[4])
