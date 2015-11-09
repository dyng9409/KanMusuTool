/*
There will be a drop tables script here
*/
drop table misc_stat;
drop table off_stat;
drop table def_stat;
drop table kanmusu;
create table kanmusu(
    ship_id NUMERIC,
    ship_name varchar(15),
    ship_yomi varchar(15),
    ship_eego varchar(30),
    ship_shipdex NUMERIC,
    ship_type varchar(10),
    ship_class varchar(20),
    primary key(ship_id)
);

create table def_stat(
    ship_id NUMERIC,
    stat_hp_min NUMERIC,
    stat_hp_max NUMERIC,
    stat_arm_min NUMERIC,
    stat_arm_max NUMERIC,
    primary key(ship_id),
    foreign key(ship_id) references kanmusu (ship_id)
);

create table off_stat(
    ship_id NUMERIC,
    stat_fp_min NUMERIC,
    stat_fp_max NUMERIC,
    stat_torp_min NUMERIC,
    stat_torp_max NUMERIC,
    stat_aa_min NUMERIC,
    stat_aa_max NUMERIC,
    primary key(ship_id),
    foreign key(ship_id) references kanmusu (ship_id)
);

create table misc_stat(
    ship_id NUMERIC,
    stat_range NUMERIC,
    stat_speed NUMERIC,
    stat_luck_min NUMERIC,
    stat_luck_max NUMERIC,
    stat_rarity NUMERIC,
    primary key(ship_id),
    foreign key(ship_id) references kanmusu(ship_id)
);
