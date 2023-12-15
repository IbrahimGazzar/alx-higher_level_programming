#!/usr/bin/python3
"""
This script lists all cities that are in a given state
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT c.name
                    FROM states AS s, cities AS c
                    WHERE c.state_id = s.id AND s.name = %s""", (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
