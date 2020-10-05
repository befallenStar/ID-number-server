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
