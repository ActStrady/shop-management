#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/9 10:33
# @Author : ActStrady@tom.com
# @FileName : goods.py
# @GitHub : https://github.com/ActStrady/shop-management


class Goods:
    # 商品编号、商品名称、单价、数量
    def __init__(self, name, price, num):
        self.__name = name
        self.__price = price
        self.__num = num

    def __str__(self):
        pass

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_num(self):
        return self.__num
