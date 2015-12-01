# -*- coding: utf-8 -*-
import dbconnect as db
import master_data

fleet = []
def database_top(): 
    print '----------'
    print '0. Exit'
    print '1. 駆逐艦 - DD Destroyer'
    #kuchikukan
    print '2. 軽巡洋艦 - CL Cruiser (Light)'
    #keijunyoukan
    #subtypes, CLT (重雷装巡洋艦) juuraisoujunyoukan, CT (練習巡洋艦) renshuu
    print '3. 重巡洋艦 - CA Cruiser (Heavy)'
    #juujunyoukan
    #subtypes, CAV (航空巡洋艦) koukuujunyoukan
    print '4. 戦艦 - BB Battleship'
    #senkan
    #subtypes, FBB (高速戦艦) kousokusenkan, BBV (航空戦艦) koukuusenkan
    print '5. 水上機母艦 - AV Seaplane Tender'
    #suijoukibokan
    print '6. 航空母艦 - CV Fleet Carriers'
    #koukuubokan
    #subtypes, CV (正規空母), CVL (型空母), CV* (装甲空母)
    #seikikuubo, keikuubo, soukoukuubo
    print '7. 潜水艦 - SS Submarine'
    #sensuikan
    #subtypes SSV (潜水空母), sensuikuubo
    print '8. 他に - Others'
    print '----------\n'
    #hoka ni
    #AS (潜水母艦) sensuibokan, LHA (ドック型揚陸艦) dokkugata yourikukan,
    #AR (工作艦) kousakukan, AO (補給油艦) hokyuuyukan
    ship_type = input('Please select a ship type: ')
    if int(ship_type) == 0:
        exit(0)
    ship_type = master_data.ship_class_top[int(ship_type)]
    print '\nYou have selected:', ship_type, '\n'
    if ship_type == u'駆逐艦' or ship_type == u'水上機母艦':
        return class_submenu(ship_type)
    else:
        return db_type_submenu(ship_type)
    #DD and AV have no subtype

def db_type_submenu(topCategory):
    #db.conn = connection
    #db.cur = cursor

    #master_data.ship_class_sub
    ind = 1
    print '----------'
    print "0. 戻る - Return"
    for elt in master_data.ship_class_sub[topCategory]:
        eego = master_data.ship_class_eego[elt]
        print str(ind)+'. '+elt+' - '+eego
        ind += 1
    print '----------\n'
    c = input("Please select the sub-type: ")
    if int(c) == 0:
        return database_top()
    choice = master_data.ship_class_sub[topCategory][int(c)-1]
    print "\nYou have selected: ", choice, '\n'

    if class_submenu(choice) is None:
        return db_type_submenu(topCategory)
    else:
        return

def class_submenu(ship_type):
    #db.conn = connection
    #db.cur = cursor
   
    query = "select distinct ship_name,ship_eego from kanmusu where ship_type = %s order by ship_name;"
    db.cur.execute(query, [ship_type])

    results = db.cur.fetchall()
    index = 1
    print "----------"
    print "O. 戻る - Return"
    for elt in results:
        print str(index)+'. '+elt[0]+' - '+elt[1]
        index += 1
    print "----------\n"
    ship = input("Please select the ship you wish to fetch: ")
    if int(ship) == 0:
        return None
    ship = results[int(ship)-1][0]
    print "\nYou have selected: ", ship, "\n"
    return getShip(ship)

def getShip(ship):

    query = """
    select *
        from kanmusu
            join off_stat on off_stat.ship_id = kanmusu.ship_id
        where ship_name = %s;
    """
    qvar = [ship]
    db.dictcur.execute(query, qvar)
    res = db.dictcur.fetchall()
    
    fleet.append(res[0])
    return 0

print 'Building fleet'
print 'Select 6 ships: '

combinedMinFP = 0
combinedMaxFP = 0
combinedMinTorp = 0
combinedMaxTorp = 0
combinedMinAA = 0
combinedMaxAA = 0

for x in range(0,6):
    print 'Current Fleet: '
    for elt in fleet:
        print elt['ship_name'], ' - ', elt['ship_eego']
    database_top()
for x in range(0,6):
    combinedMinFP += fleet[x]['stat_fp_min']
    combinedMaxFP += fleet[x]['stat_fp_max']

    combinedMinTorp += fleet[x]['stat_torp_min']
    combinedMaxTorp += fleet[x]['stat_torp_max']

    combinedMinAA += fleet[x]['stat_aa_min']
    combinedMaxAA += fleet[x]['stat_aa_max']
    print fleet[x]['ship_name'], ' - ', fleet[x]['ship_eego']
print 'Fleet Statistics (No Loadout): \n'
print 'Combined Minimum Firepower: ', combinedMinFP
print 'Combined Maximum Firepower: ', combinedMaxFP
print 'Combined Minimum Torpedo: ', combinedMinTorp
print 'Combined Maximum Torpedo: ', combinedMaxTorp
print 'Combined Minimum Anti-Air: ', combinedMinAA
print 'Combined Maximum Anti-Air: ', combinedMaxAA
