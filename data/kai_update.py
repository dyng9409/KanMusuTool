# -*- coding: utf-8 -*-
import psycopg2
import dbconnect as db
import re
#db.conn
#db.cur

searchQuery = 'select ship_id, ship_eego, ship_yomi from kanmusu where ship_name like %s;'
q1 = ['%改']
db.cur.execute(searchQuery, q1)
rows = db.cur.fetchall()
for elt in rows:
    print elt[0], elt[1], elt[2]
    searchQuery = 'update kanmusu set ship_eego = %s, ship_yomi = %s where ship_id = %s;'
    qvars = [elt[1]+' kai', elt[2]+u'かい'.encode('utf-8'), elt[0]]
    db.cur.execute(searchQuery, qvars)
    db.conn.commit()

print 'kai done'
searchQuery = 'select ship_id, ship_eego, ship_yomi from kanmusu where ship_name like %s;'
q2 = ['%改二']
db.cur.execute(searchQuery, q2)
rows = db.cur.fetchall()
for elt in rows:
    print elt[0], elt[1], elt[2]
    searchQuery = 'update kanmusu set ship_eego = %s, ship_yomi = %s where ship_id = %s;'
    qvars = [elt[1]+' kai ni', elt[2]+u'かいに'.encode('utf-8'), elt[0]]
    db.cur.execute(searchQuery, qvars)
    db.conn.commit()
