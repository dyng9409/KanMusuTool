# -*- coding: utf-8 -*-
import dbconnect as db
import master_data
def database_top(): 
    print '1. 駆逐艦 - Destroyer'
    #kuchikukan
    print '2. 軽巡洋艦 - Cruiser (Light)'
    #keijunyoukan
    #subtypes, CLT (重雷装巡洋艦) juuraisoujunyoukan, CT (練習巡洋艦) renshuu
    print '3. 重巡洋艦 - Cruiser (Heavy)'
    #juujunyoukan
    #subtypes, CAV (航空巡洋艦) koukuujunyoukan
    print '4. 戦艦 - Battleship'
    #senkan
    #subtypes, FBB (高速戦艦) kousokusenkan, BBV (航空戦艦) koukuusenkan
    print '5. 水上機母艦 - Seaplane Tender'
    #suijoukibokan
    print '6. 航空母艦 - Fleet Carriers'
    #koukuubokan
    #subtypes, CV (正規空母), CVL (型空母), CV* (装甲空母)
    #seikikuubo, keikuubo, soukoukuubo
    print '7. 潜水艦 - Submarine'
    #sensuikan
    #subtypes SSV (潜水空母), sensuikuubo
    print '8. 他に - Others'
    #hoka ni
    #AS (潜水母艦) sensuibokan, LHA (ドック型揚陸艦) dokkugata yourikukan,
    #AR (工作艦) kousakukan, AO (補給油艦) hokyuuyukan
    ship_type = input('Please select a ship type: ')
    ship_type = master_data.ship_class_top[int(ship_type)]
    print 'You have selected:', ship_type
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
    for elt in master_data.ship_class_sub[topCategory]:
        eego = master_data.ship_class_eego[elt]
        print str(ind)+'. '+elt+' - '+eego
        ind += 1
    c = input("Please select the sub-type: ")
    choice = master_data.ship_class_sub[topCategory][int(c)-1]
    
    return class_submenu(choice)
   
def class_submenu(ship_type):
    #db.conn = connection
    #db.cur = cursor
   
    query = "select distinct ship_name,ship_eego from kanmusu where ship_type = %s order by ship_name;"
    db.cur.execute(query, [ship_type])

    results = db.cur.fetchall()
    index = 1
    for elt in results:
        print str(index)+'. '+elt[0]+' - '+elt[1]
        index += 1
    ship = input("Please select the ship you wish to view: ")
    ship = results[int(ship)-1][0]
    return ship_info(ship)

def ship_info(ship):

    query = """
    select *
        from kanmusu
            join off_stat on off_stat.ship_id = kanmusu.ship_id
            join def_stat on def_stat.ship_id = kanmusu.ship_id
            join misc_stat on misc_stat.ship_id = kanmusu.ship_id
        where ship_name = %s;
    """
    qvar = [ship]
    db.dictcur.execute(query, qvar)
    res = db.dictcur.fetchall()
    for key, val in res[0].iteritems():
        print key+': ', val
