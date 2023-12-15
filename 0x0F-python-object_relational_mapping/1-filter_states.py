#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""

# Required imports
import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the database
    db = MySQLdb.connect(
        user=sys.argv[1],    # MySQL username
        passwd=sys.argv[2],  # MySQL password
        db=sys.argv[3]       # Database name
    )

    # Creating a cursor to execute SQL queries
    c = db.cursor()

    # Executing a SELECT query to retrieve states starting with 'N'
    c.execute("SELECT `id`, `name` FROM `states` WHERE `name` LIKE 'N%' "
              "ORDER BY `id` ASC")

    # Fetching all rows from the executed query
    states = c.fetchall()

    # Displaying each retrieved state
    for state in states:
        print(state)
