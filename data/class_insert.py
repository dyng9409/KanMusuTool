# -*- coding: utf-8 -*-
import psycopg2
import dbconnect as db
import re

#db.conn = connections
#db.cur = cursor

searchQuery = 'select ship_name from kanmusu where ship_eego = %s and ship_name not like %s;'
f = open('class_data.txt')
#opening line
print f.readline()
#first class
className = ''
for line in f:
    if line == '\n':
        print '----------'
        className = ''
        continue
    elif line[-2] is '|':
        className = line[0:-4]
        searchQueryVars = [className, '%改%']
        db.cur.execute(searchQuery, searchQueryVars)
        try:
            rows = db.cur.fetchall()
            className = rows[0][0] + '型'
            print className
        except:
            print 'manually change: '+className
            className = ''
    elif className == '':
        continue
    else:
        shipName = [line[0:-1]]
        #select all ships with name like that
        #for each, update the record with appropriate ship class
        query = "select ship_id from kanmusu where ship_eego = %s;"
        db.cur.execute(query, shipName)
        rows = db.cur.fetchall()
        for elt in rows:
            query = "update kanmusu set ship_class = %s where ship_id = %s;"
            qvars = [className, elt[0]]
            db.cur.execute(query, qvars)
            db.conn.commit()

# x = ['classname']
#sql = 'select * from kanmusu where ship_eego = %s;'
#cur.execute(sql, x)
f.close()
#manually required updates:
query = "update kanmusu set ship_class = %s where ship_id = %s;"
#maestrale class: libeccio
db.cur.execute(query,['Maestrale',347])
db.conn.commit()
db.cur.execute(query,['Maestrale',443])
db.conn.commit()

#type 1934 class: z1, z3
cname = 'Type 1934'
updateList = [175, 180, 311, 174, 179, 310]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Admiral Hipper class: Prinz Eugen
cname = 'Admiral Hipper'
updateList = [176, 177]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Bismarck Class: bismarck
cname = 'Bismarck'
updateList = [171, 172, 173, 178]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Vittorio Veneto Class: littorio, roma
cname = 'Vittorio Veneto'
updateList = [441, 446, 442, 447]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Ryuuhou Class: ryuuhou
cname = '龍鳳型'
updateList = [318, 185]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Submarines
#junsen 3 class 巡潜三型: i-8
cname = '巡潜三型'
updateList = [128, 400]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#junsen b class: 1-19
cname = '巡潜乙型'
updateList = [191, 401]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#junsen b mod 2 class: i-58
cname = '巡潜乙改二型'
updateList = [127, 399]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#sen toku class special submarine: i-401
cname = '潜特型'
updateList = [155, 403]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#kaidai6gataa : imuya
cname = '海大6型a'
updateList = [126, 398]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#ro-500:
cname = '呂型'
updateList = [436]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#type 3 submergence transport: maruyu
cname = '三式潜航輸送艇'
updateList = [402, 163]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#Type IXC: yuu:
cname = 'Type IXC'
updateList = [334, 431]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#taigei class: taigei
cname = '大鯨型'
updateList = [184]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#akitsumaru
cname = '丙型'
updateList = [161, 166]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

#yuubari
cname = '夕張'
updateList = [115, 293]
for elt in updateList:
    db.cur.execute(query,[cname,elt])
    db.conn.commit()

db.cur.close()
db.conn.close()
