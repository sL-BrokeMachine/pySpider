# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 18:29
# @File   : analysis.py

import dcdRequest
from pyquery import PyQuery as pq


def analysisSalesRank(month, count, tableField: list):
    """
    筛选汽车销量排行榜返回的JSON数据
    :param month:日期(500:半年；1000:一年；202111:2021年11月)
    :param count:一次请求的数据量
    :param tableField:所需要的数据字段名(type:list)
    :return:list
    """
    infos = dcdRequest.getSalesRank(month, count)['data']['list']
    result = []
    for info in infos:
        dic = {}
        for key, val in info.items():
            if (key in tableField):
                dic[key] = val
        result.append(dic)
    return result


def analysisScore(seriesId, seriesName, *tableField: list):
    """
    对懂车分页面进行解析
    :param seriesId:每辆汽车对应的series_id
    :param seriesName:每辆汽车的名称
    :param tableField:所需要的数据字段名(type:list)
    :return:list
    """
    doc = pq(dcdRequest.getScore(seriesId))
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
    pass
