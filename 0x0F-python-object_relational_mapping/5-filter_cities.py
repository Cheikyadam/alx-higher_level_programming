#!/usr/bin/python3
"""first code"""
import MySQLdb
import sys
if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
            """SELECT cities.name
            FROM cities INNER JOIN states ON
            states.id=cities.state_id
            WHERE states.name=%s
            ORDER BY cities.id ASC""", (sys.argv[4],))
    query_rows = cur.fetchall()
    cities = ''
    for row in query_rows:
        cities += row[0] + ', '
    cities = cities[:-2]
    print(cities)
    cur.close()
    conn.close()
