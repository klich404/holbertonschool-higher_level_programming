#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         charset="utf8")

    """prepare object cursor with cursor()"""
    cursor = db.cursor()

    """execute SQL query with execute()"""
    cursor.execute("SELECT cities.name FROM states INNER JOIN cities ON\
        cities.state_id = states.id WHERE\
            states.name = %s", (argv[4], ))

    """Fetch all the rows with fetchall()"""
    rows = cursor.fetchall()

    print(", ".join(row[0] for row in rows))

    """disconnect from server"""
    cursor.close()
    db.close()
