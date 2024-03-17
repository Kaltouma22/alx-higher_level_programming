#!/usr/bin/python3
"""Lists states from hbtn_0e_0_usa where the name matches the argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
