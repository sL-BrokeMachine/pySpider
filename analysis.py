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
    pass
