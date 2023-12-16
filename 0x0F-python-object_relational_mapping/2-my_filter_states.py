#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

# Required imports
import sys
import MySQLdb

if __name__ == "__main__":

    # Establishing a connection to the database
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Creating a cursor to execute SQL queries
    c = db.cursor()

    # Execute a query to fetch states based on the provided state name
    c.execute("SELECT * FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Displaying each value in the states
    states = c.fetchall()
    for state in states:
        print(state)
