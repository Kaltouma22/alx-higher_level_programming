#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
