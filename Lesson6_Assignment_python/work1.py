#方法一
import requests
from bs4 import BeautifulSoup

# 以前遇到过的函数

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

#筛选保存数据到文件            
def save(data, file):
    for i in data:
        data1 = '\t'.join(i)+'\n'
        import re
        m = re.search('质量等级|优|良',data1)
        if m == None:
            pass
        else:
            with open(file,'a') as f:
                f.write(data1) 
        
    print('data saved in ', file)
    

if __name__ == '__main__':
    datas = []
    for i in range(1, 2):
        url = build_url('hangzhou', 2019, i)
        data = parse(url, '杭州')
        datas.extend(data)
    
    save(data, 'D:\data.txt')
    
    
#方法二
import requests
from bs4 import BeautifulSoup

# 以前遇到过的函数

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

#筛选保存数据到文件            
def save(data, file):
    def func(x):
        if '质量等级' in x or '优' in x or '良' in x:
            return True
        else:
            return False
    data1 = list(filter(func,data))
    f = open(file,'a')
    for i in data1:
        data2 = '\t'.join(i)+'\n'
        f.write(data2)
    f.close()
        
    print('data saved in ', file)
    

if __name__ == '__main__':
    datas = []
    for i in range(1, 2):
        url = build_url('hangzhou', 2019, i)
        data = parse(url, '杭州')
        datas.extend(data)
    
    save(data, 'D:\data.txt')
