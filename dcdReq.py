# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 10:42
# @File   : dcdReq.py
import requests
import json


def requestData(url):
    """
    封装请求函数
    :param url: 请求地址
    :return: 将请求结果全部返回
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'cookie': 'msToken=-s47EZoJ60RImLkP85fuulrgriS8L-qlSXK6XwfG2CH2cQqp-3qv3-RLtnuYigcA4YoabQ_sut1TFy_e_1DvHGpqNzJd_ESmm_Z2o22m5HJ1'
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
    except BaseException as e:
        print(f"数据请求异常🤡  {e}")
    else:
        if (response.status_code == 200):
            print(f"{url} 请求成功☺")
            return response.text
        else:
            print("请求失败")
            return 0


def getSalesRank(month, count):
    """
    获得新能源汽车销售排行
    :param month: 时间(500：半年；1000：一年)
    :param count: 每一页最多显示数据量
    :return:JSON数据
    """
    url = f"https://www.dongchedi.com/motor/pc/car/rank_data?new_energy_type=1&month={month}&count={count}&rank_data_type=11"
    response = requestData(url)
    if (response != 0):
        # 将结果转换成JSON格式
        return json.loads(response)


def getScore(seriesId):
    """
    请求汽车评分页面
    :param seriesId: 汽车series_id
    :return:网页HTML
    """
    url = f"https://www.dongchedi.com/auto/series/score/{seriesId}-x-x-x-x-x-x"
    response = requestData(url)
    if (response != 0):
        return response


if __name__ == '__main__':
    pass
