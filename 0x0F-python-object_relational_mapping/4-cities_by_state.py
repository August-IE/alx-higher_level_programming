#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
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
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` "
              "FROM `cities` as `c` "
              "INNER JOIN `states` as `s` "
              "ON `c`.`state_id` = `s`.`id` "
              "ORDER BY `c`.`id`")

    # Displaying each value in the states
    states = c.fetchall()
    for city in states:
        print(city)
