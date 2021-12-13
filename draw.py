# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/12/7 9:40
# @File   : draw.py
import os
import webbrowser
import dataStorage as db
from pyecharts import options as opts
from pyecharts.charts import Bar, WordCloud, Page, Line


# 绘制近一年汽车销量榜
def draw():
    width = "1650px"
    height = "820px"
    pageTitle = "数据展示页面"
    page = Page(layout=Page.SimplePageLayout, page_title=pageTitle)
    # 每个厂商销量汇总
    xAxis = []
    yAxis = []
    sql = "SELECT `brand_name`, GROUP_CONCAT( series_name ) AS 'series_names',SUM( count ) AS 'brand_count' FROM car_info GROUP BY car_info.brand_name ORDER BY SUM( count ) DESC"
    infos = db.queryData('car_info', sql)

    for info in infos:
        xAxis.append(info["brand_name"])
        yAxis.append(info['brand_count'])

    bar_1 = (
        Bar(
            init_opts=opts.InitOpts(width=width, height=height, page_title=pageTitle)
        )
            .add_xaxis(xAxis)
            .add_yaxis('', yAxis)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            yaxis_opts=opts.AxisOpts(name='销量(台)'),
            title_opts=opts.TitleOpts(title=f"近一年汽车品牌销量表"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    page.add(bar_1)

    # 获取每个厂商最高销量车型
    xAxis = []
    yAxis = []
    sql = "SELECT *, MAX(count) AS max_count_brand FROM car_info GROUP BY `brand_name`"
    infos = db.queryData('car_info', sql)

    for info in infos:
        xAxis.append(f'{info["brand_name"]}-{info["series_name"]}')
        yAxis.append(info['max_count_brand'])

    bar_2 = (
        Bar(
            init_opts=opts.InitOpts(width=width, height=height)
        )
            .add_xaxis(xAxis)
            .add_yaxis('', yAxis)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            yaxis_opts=opts.AxisOpts(name='销量(台)'),
            title_opts=opts.TitleOpts(title=f"每个品牌最高销量表"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    page.add(bar_2)

    # 词云
    data = []
    infos = db.queryData('car_info')
    for info in infos:
        result = []
        result.append(info['series_name'])
        result.append(info['count'])
        data.append(tuple(result))

    c = (
        WordCloud(
            init_opts=opts.InitOpts(width=width, height=height),
        )
            .add(
            series_name="车型销量",
            data_pair=data,
            word_size_range=[5, 700],
            width=width,
            height=height,
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="汽车销量词云",
                title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    page.add(c)

    # 懂车分排行榜
    xData = []
    yData = []
    # 获取x轴，y轴数据
    infos = db.queryData('score')
    comment = db.queryData('score', 'SHOW CREATE TABLE score')
    for k in comment:
        # 替换反斜杠,使用\\。替换换行符\n,使用下面的
        structure = eval(repr(k["Create Table"]).replace('\\n  ', ''))
        # 使用COMMENT切割
        res = structure.split("COMMENT")
        for r in res[1:len(res) - 1]:
            xData.append(r.split()[0].split(',')[0].strip('\''))

    for info in infos:
        if info['composite'] != '-':
            yData.append(list(info.values())[2:len(info) - 1])

    line = (
        Line(
            init_opts=opts.InitOpts(width=width, height=height, )
        )
            .add_xaxis(xaxis_data=xData[3:])
            .add_yaxis(
            series_name=f'{yData[0][0]}',
            y_axis=yData[0][1:],
        )
            .add_yaxis(
            series_name=f'{yData[1][0]}',
            y_axis=yData[1][1:],
        )
            .add_yaxis(
            series_name=f'{yData[2][0]}',
            y_axis=yData[2][1:],
        )
            .add_yaxis(
            series_name=f'{yData[3][0]}',
            y_axis=yData[3][1:],
        )
            .add_yaxis(
            series_name=f'{yData[4][0]}',
            y_axis=yData[4][1:],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="部分懂车分展示"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts={"interval": "0", "rotate": -20},  # X轴显示间隔
            ),
        )
    )

    page.add(line)
    link = f'{os.getcwd()}\\display\\show.html'
    page.render(link, )
    print("图表绘制完成😀")
    return link


if __name__ == '__main__':
    webbrowser.open(draw())
