#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

# Required imports
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Establishing a connection to the database
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host='localhost',
    )

    # Creating a cursor to execute SQL queries
    c = db.cursor()

    # Execute a query to fetch states based on the provided state name
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    c.execute(query, (state_name,))

    # Displaying each value in the states
    states = c.fetchall()
    for state in states:
        print(state)

    # Close the database connection
    db.close()
