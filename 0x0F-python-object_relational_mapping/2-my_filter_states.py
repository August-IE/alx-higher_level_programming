#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

# Required imports
import sys
import MySQLdb

if __name__ == "__main__":

    # Extracting command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Establishing a connection to the database
        db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost'  # The default localhost
        )

        # Creating a cursor to execute SQL queries
        c = db.cursor()

        # Executing a SELECT query to retrieve states
        c.execute("SELECT `id`, `name` FROM `states` WHERE BINARY `name` = %s",
                  (state_name,))

        # Fetching all rows from the executed query
        states = c.fetchall()

        # Displaying each retrieved state
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if 'db' in locals() and db.open:
            db.close()
