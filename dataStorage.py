# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 20:25
# @File   : dataStorage.py

# 🔨该文件的代码还存在BUG，待修复完善

import pymysql

host = "127.0.0.1"
user = "root"
password = "password"
database = "databases"

try:
    db = pymysql.connect(host=host, user=user, password=password, database=database)
except BaseException as e:
    print(f"数据库连接异常🤡  {e}")
else:
    print("数据库连接异常🤡")


# 生成SQL语句
def getSql(tableName, tableData, operation):
    # 生成字段`
    cols = ','.join(f'`{key}`' for key in tableData.keys())
    values = ','.join(f'%({key})s' for key in tableData.keys())
    sql = ''
    if (operation.upper() == 'INSERT'):
        sql = f'INSERT INTO {tableName}({cols})VALUES ({values})'
    return sql


def insertData(tableName, tableData: list):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 1、判断插入的数据记录是否在表中
    for data in tableData:
        querySql = f'SELECT `series_id` FROM {tableName} WHERE `series_id` = {data["series_id"]}'
        cursor.execute(querySql)
        result = cursor.fetchall()
        # 判断数据是否存在
        if result:
            # 如果存在只对其更新数据
            updateData(tableName, data)
            print(f"数据更新成功 {data['series_id']}")
        else:
            # 如果不存在直接插入数据
            insterSql = getSql(tableName, data, 'INSERT')
            try:
                cursor.execute(insterSql, data)
                # 提交
                db.commit()
                print(f"数据插入成功 {data['series_id']}")
            except pymysql.Error as e:
                print(e.args[0], e.args[1])
                print("数据插入失败！！")
                # 发生错误时回滚
                db.rollback()


def updateData(tableName, dataDic):
    """
    将score和brand_name插入表中
    :param tableName:
    :param dataDic:
    :return:
    """
    val = ', '.join(f'`{key}`="{val}"' for key, val in dataDic.items())
    updateSql = f'UPDATE {tableName} SET {val} WHERE `series_id` = {dataDic["series_id"]}'
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行SQL语句
    cursor.execute(updateSql)
    db.commit()


def queryData(tableName, querySql=''):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if querySql:
        cursor.execute(querySql)
        db.commit()
        return cursor.fetchall()
    else:
        querySql = f"SELECT * FROM {tableName}"
        cursor.execute(querySql)
        db.commit()
        return cursor.fetchall()


if __name__ == '__main__':
    sql = "SELECT brand_name, GROUP_CONCAT( series_name ) AS 'series_names',SUM( count ) AS 'brand_count' FROM car_info GROUP BY car_info.brand_name ORDER BY SUM( count ) DESC"
    print(queryData('car_info', sql))
    pass
