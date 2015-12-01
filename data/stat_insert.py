import json, romkan
import psycopg2

execfile('jsonify.py')
#ships = master ship list
f = open('pwd.txt')
user = f.readline().strip()
pwd = f.readline().strip()
connect_name = "dbname='kancolle' user='"+user+"' host='localhost' password='"+pwd+"'"
conn = psycopg2.connect(connect_name)
cur = conn.cursor()
print 'Updating Stats'
for ind in range(0,383):
    idnum = ships[ind]['api_id']

    hp = ships[ind]['api_taik']
    arm = ships[ind]['api_souk']

    cur.execute('INSERT INTO def_stat values(%s, %s, %s, %s, %s);',(idnum, hp[0], hp[1], arm[0], arm[1]))

    fp = ships[ind]['api_houg']
    torp = ships[ind]['api_raig']
    aa = ships[ind]['api_tyku']

    cur.execute('INSERT INTO off_stat values(%s, %s, %s, %s, %s, %s, %s);',(idnum, fp[0], fp[1], torp[0], torp[1], aa[0], aa[1]))

    rng = ships[ind]['api_leng']
    spd = ships[ind]['api_soku']
    lck = ships[ind]['api_luck']
    rare = ships[ind]['api_backs']

    cur.execute('INSERT INTO misc_stat values(%s, %s, %s, %s, %s, %s);',(idnum, rng, spd, lck[0], lck[1], rare))


conn.commit()
cur.close()
conn.close()

