#!/usr/bin/python3
# A script that lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> "
              "<database name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        c = db.cursor()

        c.execute("SELECT `id`, `name` FROM `states` "
                  "ORDER BY `states`.`id` ASC")
        states = c.fetchall()
        for state in states:
            print(state)

        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
