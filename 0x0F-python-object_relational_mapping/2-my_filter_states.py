#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = conn.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(user_input)
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
