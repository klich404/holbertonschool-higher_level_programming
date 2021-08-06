#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                    user=argv[1], password=argv[2], db=argv[3], charset="utf8")

    """prepare object cursor with cursor()"""
    cursor = db.cursor()

    """execute SQL query with execute()"""
    cursor.execute("SELECT * FROM states WHERE name = %s", (argv[4],))

    """Fetch all the rows with fetchall()"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """disconnect from server"""
    cursor.close()
    db.close()
