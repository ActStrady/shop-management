#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/9 10:42
# @Author : ActStrady@tom.com
# @FileName : goods_dao.py
# @GitHub : https://github.com/ActStrady/shop-management
import sqlite3


class GoodsDao:
    connection = sqlite3.connect('sqllite/goods.sqlite')
    cursor = connection.cursor()

    def add(self, goods):
        self.cursor.execute('insert into goods values(null, ?, ?, ?)', (goods.get_name(), goods.get_price(),
                                                                        goods.get_num()))

    def query_all(self):
        self.cursor.execute('select * from goods')
        values = self.cursor.fetchall()
        return values

    def query_by_name(self, name):
        self.cursor.execute('select * from goods where name=?', (name,))
        values = self.cursor.fetchall()
        return values
