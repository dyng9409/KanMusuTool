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
    db_type_submenu(ship_type)
    #DD and AV have no subtype
    return

def db_type_submenu(topCategory):
    #db.conn = connection
    #db.cur = cursor

    #master_data.ship_class_sub
    ind = 1
    for elt in master_data.ship_class_sub[topCategory]:
        eego = master_data.ship_class_eego[elt]
        print str(ind)+'. '+elt+' - '+eego
        ind += 1
    #ideally, form here we go to ship class, but that requires processing
    return
    
