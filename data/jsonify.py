import json, re

f = open('output.txt')
r = f.read()
f.close()

data = re.sub('svdata=','',r)

final = json.loads(data)['api_data']

ships = final['api_mst_ship']
