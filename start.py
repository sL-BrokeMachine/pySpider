# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/27 16:38
# @File   : start.py
import webbrowser
import analysis
import dataStorage
import draw
from concurrent.futures import ThreadPoolExecutor

tableField = ['series_id', 'brand_name', 'series_name', 'min_price', 'max_price', 'count']
scoreTable = ['series_id', 'series_name', 'composite', 'appearance', 'interior', 'configure', 'space', 'comfort',
              'manipulation', 'power']

mount = 1000  # 一年
count = 100

# 获取汽车销量榜
result = analysis.analysisSalesRank(mount, count, tableField)
# 数据存储
dataStorage.insertData('car_info', result)

# 获取懂车分
## 通过数据库获得series_id
infos = dataStorage.queryData('car_info')
# 创建线程池
executor = ThreadPoolExecutor(max_workers=30)
tasks = []
for info in infos:
    # 通过submit函数提交执行的函数(analysis.analysisScore)到线程池中，submit函数立即返回，不阻塞
    tasks.append(executor.submit(analysis.analysisScore, info['series_id'], info['series_name'], scoreTable))

# result方法可以获取task的执行结果
scoreRes = [task.result() for task in tasks]
executor.shutdown(wait=True)
# 将结果存储到数据库中
dataStorage.insertData('score', scoreRes)

# 绘制展示图
webbrowser.open(draw.draw())