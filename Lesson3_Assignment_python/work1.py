!pip install bs4

import requests
from bs4 import BeautifulSoup

def build_url(city_coding, year=None, month=None):
    """
    创建网页链接
    paramters:
        city_coding: 城市名称(英文)
        year: 年份
        month: 月份
    return:
        url: 可访问的链接
    """
    BASE = 'http://www.tianqihoubao.com/aqi/'
    city_base_url = BASE + '{}.html'
    city_date_base_url = BASE + '{}-{}{}.html'
    
    if year is not None and month is not None:
        month = str(month) if month >= 10 else '0' + str(month)
        return city_date_base_url.format(city_coding, year, month)
    else:
        return city_base_url.format(city_coding)


def parse(url, city_name):
    """
    抓取网页信息
    parameters:
        url: 需要抓取的网页链接
        city_name: 城市名称(用于数据标识)
    returns:
        result: 抓取的信息
    """
    response = requests.get(url)
    if response.ok:
        html = response.text
        
        soup = BeautifulSoup(html)
        data_table = soup.table
        
        content = data_table.contents
        
        result = []
        for index, c in enumerate(content[1::2]):
                if index == 0:
                    result.append(tuple(['城市'] + c.text.split()))
                else:
                    result.append(tuple([city_name] + c.text.split()))
        return result
    
    else:
        if response.status_code == 403:
            print('403 Forbidden! 抓取太快你被拉黑啦~')
            
all_data = []
for i in range(1,13):
    url1 = build_url('hangzhou',2019,i)
    all_data.append(parse(url1,'杭州'))
print(all_data)
