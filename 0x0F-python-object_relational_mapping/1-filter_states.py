#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """Fetch all the rows with fetchall()"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """disconnect from server"""
    cursor.close()
    db.close()
