import psycopg2
f = open('pwd.txt')
user = f.readline().strip()
pwd = f.readline().strip()
f.close
#ships = master ship list
connect_name = "dbname='kancolle' user='"+user+"' host='localhost' password='"+pwd+"'"
conn = psycopg2.connect(connect_name)
cur = conn.cursor()

