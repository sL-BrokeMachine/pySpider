# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 10:42
# @File   : dcdReq.py

# 数据请求

import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'cookie': 'msToken=-s47EZoJ60RImLkP85fuulrgriS8L-qlSXK6XwfG2CH2cQqp-3qv3-RLtnuYigcA4YoabQ_sut1TFy_e_1DvHGpqNzJd_ESmm_Z2o22m5HJ1'
}


def requestData(url, headers):
    """
    封装请求函数
    :param url: 请求地址
    :param headers: 带cookie值得请求头
    :return: 将请求结果全部返回
    """
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    if (response.status_code == 200):
        # print(f"请求成功  {url}")
        return response.text
    else:
        print("请求失败")
        return 0


# 1、获得主页近1年的新能源汽车销售排行
def getSalesRank(month, count):
    """
    :param month: 时间(500：半年；1000：一年)
    :param count: 每一页最多显示数据量
    :return:
    """
    # url = f"https://www.dongchedi.com/motor/pc/car/rank_data?month={month}&rank_data_type=11&offset=0&count={count}&outter_detail_type={outter_detail_type}"
    url = f"https://www.dongchedi.com/motor/pc/car/rank_data?new_energy_type=1&month={month}&count={count}&rank_data_type=11"
    response = requestData(url, headers)
    if (response != 0):
        # 将结果转换成JSON格式
        return json.loads(response)


# 2、获得每款汽车详细信息
def getCarInfos(seriesId):
    url = f"https://www.dongchedi.com/auto/series/{seriesId}"
    response = requestData(url, headers)
    if (response != 0):
        return response


# 3、得到汽车评分
def getScore(seriesId):
    url = f"https://www.dongchedi.com/auto/series/score/{seriesId}-x-x-x-x-x-x"
    response = requestData(url, headers)
    if (response != 0):
        return response


if __name__ == '__main__':
    pass
