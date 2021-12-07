# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 18:29
# @File   : analysis.py

import dcdReq
from pyquery import PyQuery as pq


# 解析汽车销量排行榜
def analysisSalesRank(month, count, tableField: list):
    infos = dcdReq.getSalesRank(month, count)['data']['list']
    result = []
    for info in infos:
        dic = {}
        for key, val in info.items():
            if (key in tableField):
                dic[key] = val
        result.append(dic)
    return result


# 获取懂车分
def analysisScore(seriesId, seriesName, *tableField: list):
    doc = pq(dcdReq.getScore(seriesId))
    elements = doc(".tw-h-94")
    score = []
    score.append(seriesId)
    score.append(seriesName)
    for element in elements.items():
        items = [li.text() for li in element.items('li')]
        score.append(items[1])
    if tableField:
        return dict(zip(tableField[0], score))
    else:
        return score


if __name__ == '__main__':
    tableField = ['series_id', 'brand_name', 'series_name', 'min_price', 'max_price', 'count', 'type']
    scoreTable = ['series_id', 'series_name', 'composite', 'appearance', 'interior', 'configure', 'space', 'comfort',
                  'manipulation', 'power']

    # 获取汽车信息
    ## 每个车型获取的数据量45条
    count = 100

    result = analysisSalesRank(1000, "测试", count, tableField)
    print(result)
    #     # 数据存储
    #     dataStorage.insertData('car_info', result)
    #
    # # 存储请求series_id的线程列表
    # requestThreadList = []
    # # 通过series_id获取懂车帝分数
    # score.txt = []
    #
    # # 通过数据库获得series_id
    # infos = dataStorage.queryData('car_info')
    #
    # for info in infos:
    #     dic = {}
    #     dic['series_id'] = info['series_id']
    #     dic = analysisScore(dic)
    #     dataStorage.updateData('car_info', dic)
    print(analysisScore({'series_id': 4499}, scoreTable))
