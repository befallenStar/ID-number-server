# -*- encoding: utf-8 -*-
from scratchData import load_data

municipality = ['11', '12', '31', '50']


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
    year = ID[6:10]
    month = ID[10:12]
    day = ID[12:14]
    days = leap_year(int(year))
    if not (0 < int(month) < 13 and 0 < int(day) < days[int(month)]):
        raise ValueError(year + month + day + ' is invalid date, '
                                              'so ' + ID + ' is an invalid ID')
    print('birthday: {}-{}-{}'.format(year, month, day))


def leap_year(year: int):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def read(ID):
    if not check_verification(ID):
        raise ValueError(ID + ' is an invalid ID')
    search_area('141082199802012327')
    extract_birthday(ID)
