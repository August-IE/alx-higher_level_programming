#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
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

    # Execute a query to fetch cities based on the provided state name
    state_name = sys.argv[4]
    c.execute("SELECT `cities`.`name` FROM `cities` "
              "INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` "
              "WHERE `states`.`name` = %s", (state_name,))

    # Fetch data from the cursor
    city_names = [ct[0] for ct in c.fetchall()]

    # Join the city names with a comma and print
    city_names_joined = ", ".join(city_names)
    print(city_names_joined)
