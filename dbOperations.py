# -*- encoding: utf-8 -*-
import pymysql


def main():
    conn=pymysql.connect(host='localhost',user='root',password='root',database='id_number',charset='utf8')
    cursor=conn.cursor()
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
    sql='''
    CREATE TABLE districts(
    id INT auto_increment primary key ,
    code char(6) not null ,
    city char(20) not null ,
    city_id int not null
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    '''
    res=cursor.execute(sql)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()