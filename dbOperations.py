# -*- encoding: utf-8 -*-
import pymysql
from scratchData import load_data

municipality = ['11', '12', '31', '50']



def main():
    conn=pymysql.connect(host='localhost',user='root',password='root',database='id_number',charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    # sql='''
    # CREATE TABLE provinces(
    # id INT auto_increment primary key ,
    # code char(2) NOT NULL,
    # city char(10) NOT NULL
    # )ENGINE=innodb DEFAULT CHARSET=utf8;
    # '''
    # sql='''
    # CREATE TABLE cities(
    # id INT auto_increment primary key ,
    # code char(6) NOT NULL ,
    # city char(20) NOT NULL ,
    # province_id INT not null ,
    # municipality bool not null default 0
    # )ENGINE=innodb DEFAULT CHARSET=utf8;
    # '''
    # sql='''
    # CREATE TABLE districts(
    # id INT auto_increment primary key ,
    # code char(6) not null ,
    # city char(20) not null ,
    # city_id int not null
    # )ENGINE=innodb DEFAULT CHARSET=utf8;
    # '''
    provinces,cities,districts=load_data()
    # for code,city in provinces.items():
    #     print(code,city)
    #     sql='''insert into provinces (code,city) values ('%s','%s');'''%(code,city)
    #     res=cursor.execute(sql)
    #     print(res)

    for code, city in cities.items():
        sql='''select * from provinces where code = %s'''
        res=cursor.execute(sql,[code[:2]])
        if res:
            # print(cursor.fetchone())
            result=cursor.fetchone()
            muni=0
            if result['code'] in municipality:
                muni=1
            # print(code, city)
            sql = '''insert into cities (code,city,province_id,municipality) values (%s,%s,%s,%s);'''
            res = cursor.execute(sql,[code,city,result['id'],muni])
            # print(res)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()