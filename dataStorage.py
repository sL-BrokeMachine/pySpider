# -*- coding: utf-8 -*-
# @Author : Loners
# @Time   : 2021/11/15 20:25
# @File   : dataStorage.py
import pymysql

host = "127.0.0.1"
user = "root"
password = "lyh3456" #修改为自己的mysql密码
database = "dongchedi"

try:
    db = pymysql.connect(host=host, user=user, password=password, database=database)
except BaseException as e:
    print(f"数据库连接异常🤡  {e}")
else:
    print("😀数据库连接成功")


def getSql(tableName, tableData: list, operation):
    """
    生成部分SQL语句
    :param tableName:数据库表的名称
    :param tableData:数据库表的列名称
    :param operation:对应的数据库操作名称
    :return:sql语句
    """
    # 生成字段
    cols = ','.join(f'`{key}`' for key in tableData.keys())
    values = ','.join(f'%({key})s' for key in tableData.keys())
    sql = ''
    if (operation.upper() == 'INSERT'):
        sql = f'INSERT INTO {tableName}({cols})VALUES ({values})'
    return sql


def insertData(tableName, tableData: list):
    """
    插入数据记录，通过`series_id`对数据的唯一性进行判断
    :param tableName:数据库表的名称
    :param tableData:数据库表的列名称
    :return:ok 或者 对应错误信息
    """
    # 使用cursor()方法获取操作游标
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 1、判断插入的数据记录是否在表中
    for data in tableData:
        querySql = f'SELECT `series_id` FROM {tableName} WHERE `series_id` = {data["series_id"]}'
        cursor.execute(querySql)
        isResult = cursor.fetchall()
        # 判断数据是否存在
        if isResult:
            # 如果存在只对其更新数据
            updateData(tableName, data)
        else:
            # 如果不存在直接插入数据
            insterSql = getSql(tableName, data, 'INSERT')
            try:
                cursor.execute(insterSql, data)
                # 提交
                db.commit()
                print(f"😀数据插入成功 {data['series_id']}")
                return 'ok'
            except pymysql.Error as e:
                print("🤡数据插入失败", e.args[0], e.args[1])
                # 发生错误时回滚
                db.rollback()
                return f'Error: {e}'


def updateData(tableName, dataDic: dict):
    """
    对数据数据库记录进行更新
    :param tableName:数据库表的名称
    :param dataDic:以字典类型传递存储数据
    :return:ok 或者 对应错误信息
    """
    val = ', '.join(f'`{key}`="{val}"' for key, val in dataDic.items())
    updateSql = f'UPDATE {tableName} SET {val} WHERE `series_id` = {dataDic["series_id"]}'
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行SQL语句
        cursor.execute(updateSql)
        db.commit()
        print(f"😀数据更新成功 {dataDic['series_id']}")
        return 'ok'
    except pymysql.Error as e:
        print("🤡数据更新失败", e.args[0], e.args[1])
        # 发生错误时回滚
        db.rollback()
        return f'Error: {e}'


def queryData(tableName, querySql=''):
    """
    数据查询
    :param tableName:数据库表的名称
    :param querySql:自定义SQL语句
    :return:list
    """
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
    pass
