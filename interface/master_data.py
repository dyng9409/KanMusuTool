# -*- coding: utf-8 -*-
ship_class_top = {
        1:u'駆逐艦',
        2:u'軽巡洋艦',
        3:u'重巡洋艦',
        4:u'戦艦',
        5:u'水上機母艦',
        6:u'航空母艦',
        7:u'潜水艦',
        8:u'他'
        }

ship_class_sub = {
        u'駆逐艦':[],
        u'軽巡洋艦':[u'軽巡洋艦',u'重雷装巡洋艦',u'練習巡洋艦'],
        u'重巡洋艦':[u'重巡洋艦',u'航空巡洋艦'],
        u'戦艦':[u'戦艦',u'高速戦艦',u'航空戦艦'],
        u'水上機母艦':[],
        u'航空母艦':[u'正規空母',u'軽空母',u'装甲空母'],
        u'潜水艦':[u'潜水艦',u'潜水空母'],
        u'他':[u'潜水母艦',u'揚陸艦',u'工作艦',u'補給艦']
        }

ship_class_eego = {
        u'駆逐艦':'DD Destroyer',
        u'軽巡洋艦':'CL Cruiser (Light)',
        u'重巡洋艦':'CA Cruiser (Heavy)',
        u'戦艦':'BB Battleship',
        u'水上機母艦':'AV Seaplane Tender',
        u'航空母艦':'CV Fleet Carrier',
        u'潜水艦':'SS Submarine',
        u'他':'Others',
        u'重雷装巡洋艦':'CLT Torpedo Cruiser',
        u'練習巡洋艦':'CT Practice Cruiser',
        u'航空巡洋艦':'CAV Aviation Cruiser',
        u'高速戦艦':'FBB Fast Battleship',
        u'航空戦艦':'BBV Aviation Battleship',
        u'正規空母':'CV Standard Aircraft Carrier',
        u'軽空母':'CVL Light Aircraft Carrier',
        u'装甲空母':'CVB Armored Aircraft Carrier',
        u'潜水空母':'SSV Submarine Aircraft Carrier',
        u'潜水母艦':'AS Submarine Tender',
        u'揚陸艦':'LHA Amphibious Assault Ship',
        u'工作艦':'AR Repair Ship',
        u'補給艦':'AO Fleet Oiler'
        }

