# -*- encoding: utf-8 -*-
import re

import requests

municipality = ['11', '12', '31', '50']


def load_data():
    response = requests.get(
        url='http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html')
    pattern = re.compile('>[\d\u4e00-\u9fa5]+<')
    code_list = pattern.findall(response.text)
    code_list = code_list[6:]
    provinces, cities, districts = {}, {}, {}
    for step in range(0, len(code_list), 2):
        code = re.findall('\d{6}', code_list[step])[0]
        city = re.findall('[\u4e00-\u9fa5]+', code_list[step + 1])[0]
        if code[2:] == '0000':
            if code[0] not in provinces.keys():
                provinces[code[0]] = {}
            provinces[code[0]][code[:2]] = city
        elif code[4:] == '00':
            if code[:2] not in cities.keys():
                cities[code[:2]] = {}
            cities[code[:2]][code[:4]] = city
        else:
            if code[:2] in municipality:
                if code[:2] not in cities.keys():
                    cities[code[:2]] = {}
                cities[code[:2]][code] = city
            else:
                if code[:4] not in districts.keys():
                    districts[code[:4]] = {}
                districts[code[:4]][code] = city
    return provinces, cities, districts


def check_verification(ID: str) -> bool:
    check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum(
        [int(ID[i]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][i]
         for i in range(17)]) % 11]
    return check_code == ID[-1]


def search_area(ID):
    provinces, cities, districts = load_data()
    ID_area = ID[:6]
    area = ''
    if ID_area[0] in provinces.keys():
        if ID_area[:2] in provinces[ID_area[0]].keys():
            province = provinces[ID_area[0]][ID_area[:2]]
            if ID_area[:2] in municipality:
                if ID_area in cities[ID_area[:2]].keys():
                    area = province + cities[ID_area[:2]][ID_area]
            else:
                if ID_area[:4] in cities[ID_area[:2]].keys():
                    city = cities[ID_area[:2]][ID_area[:4]]
                    if ID_area in districts[ID_area[:4]].keys():
                        area = province + city + districts[ID_area[:4]][ID_area]
    if area == '':
        print('wrong')
    else:
        print(area)


def extract_birthday(ID):
    year=ID[6:10]
    month=ID[10:12]
    day=ID[12:14]
    days=leap_year(int(year))
    if not (0<int(month)<13 and 0<int(day)<days[int(month)]):
        raise ValueError(year+month+day+' is invalid date, '
                                        'so '+ID+' is an invalid ID')
    print('birthday: {}-{}-{}'.format(year,month,day))


def leap_year(year:int):
    if year%400==0 or (year%4==0 and year%100!=0):
        return [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        return [31,28,31,30,31,30,31,31,30,31,30,31]


def read(ID):
    if not check_verification(ID):
        raise ValueError(ID+' is an invalid ID')
    search_area('141082199802012327')
    extract_birthday(ID)


def main():
    try:
        ID='141082199802012327'
        read(ID)
        ID='320101199801012314'
        read(ID)
        ID='141082190002292381'
        read(ID)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
