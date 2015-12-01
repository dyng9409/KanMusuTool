import json, romkan
import psycopg2

execfile('jsonify.py')
f = open('pwd.txt')
user = f.readline().strip()
pwd = f.readline().strip()
f.close
#ships = master ship list
connect_name = "dbname='kancolle' user='"+user+"' host='localhost' password='"+pwd+"'"
conn = psycopg2.connect(connect_name)
cur = conn.cursor()
stypes = final['api_mst_stype']
for ind in range(0,383):
    idnum = ships[ind]['api_id']
    sortno = ships[ind]['api_sortno']
    name = ships[ind]['api_name']
    yomi = ships[ind]['api_yomi']
    eego = romkan.to_roma(yomi)
    classind = ships[ind]['api_stype']-1
    print 'INSERTING: ', idnum,' ', name
    if classind == 7:
        shipclass = u'\u9ad8\u901f\u6226\u8266'
    else:
        shipclass = stypes[classind]['api_name']
    cur.execute('insert into kanmusu values(%s,%s,%s,%s,%s,%s);',(idnum,name,yomi,eego,sortno,shipclass))

conn.commit()
cur.close()
conn.close()

