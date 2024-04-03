"""
dbCode.py
Author: Grace Bero

Description: This is where all of the functions related to the sql database and dynamoDB 
are located. 
"""

import creds
import pymysql

'''
get_con()

@return conn, the needed information to connect to the sql databse

Credits: This was created by Professor Tim Urness and given during class
'''
def get_conn():
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        )
    return conn

'''
execute_query(query, args=())

@param query, the sql query

Executes an sql query
Credits: This was created by Professor Tim Urness and given during class
'''
def execute_query(query, args=()):
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

'''
display_db(rows)

@param rows, an SQL Query output to be displayed in the desired format
@return html, a string that creates an html table 

used to create an html table from an sql query 
'''
def display_db(rows):
    html = ""
    html += """<table><tr><th>Name</th><th>Region</th><th>Weapon</th><th>Artifacts</th><th>Release</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td><td>" + str(r[3]) + "</td><td>" + str(r[4]) + "</td>"
    html += "</table>"
    return html
             
             