#!/usr/bin/python3
"""
Script to retrieve and display all states from the hbtn_0e_0_usa database.
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
    
    # Executing a SELECT query to retrieve columns from the 'states' table
    c.execute("SELECT `id`, `name` FROM `states` ORDER BY `states`.`id` ASC")
    
    # Fetching all rows from the executed query
    states = c.fetchall()
    
    # Displaying each retrieved state
    for state in states:
        print(state)
