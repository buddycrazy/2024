import time

import requests
import json
import re


def get_sales_number(url):
    # 发送 GET 请求
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 提取 JSONP 中的 JSON 数据
    jsonp_text = response.text
    json_data = re.search(r'jQueryJSONP_stock_getStockInfo\((.*)\)', jsonp_text).group(1)

    # 解析 JSON 数据
    data = json.loads(json_data)
    # print(data)

    # 提取 salesNumber 的数值
    if data and isinstance(data, list) and 'salesNumber' in data[0]:
        sales_number = data[0]['salesNumber']
        return sales_number
    else:
        return "无法获取 salesNumber"


# 示例用法
url = 'https://papi.lenovo.com.cn/stock/getStockInfo.jhtm?ss=588&callback=jQueryJSONP_stock_getStockInfo&proInfos=%5B%7BactivityType%3A0%2C+productCode%3A1039473%7D%5D&_=1725023405154'

while True:
    sales_number = get_sales_number(url)
    if int(sales_number) > 0:
        print(f"500补货了，库存还剩: {sales_number}")
    time.sleep(1)
