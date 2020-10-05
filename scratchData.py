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
            provinces[code[:2]] = city
        elif code[4:] == '00':
            cities[code[:4]] = city
        else:
            if code[:2] in municipality:
                cities[code] = city
            else:
                districts[code] = city
    # provinces = {'11' : '北京市', ...}
    # cities = {'110101' : '东城区', ..., '1301' : '石家庄市', ...}
    # districts = {'130102' : '长安区', ...}
    return provinces, cities, districts
