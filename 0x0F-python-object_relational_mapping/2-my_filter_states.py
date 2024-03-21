#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    try:
        # Execute the SQL command
        cursor.execute(sql, (state_name,))
        # Fetch all the rows in a list of lists
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # Disconnect from server
    db.close()
