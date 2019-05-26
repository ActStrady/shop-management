#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/9 11:21
# @Author : ActStrady@tom.com
# @FileName : main.py
# @GitHub : https://github.com/ActStrady/shop-management
from dao import goods_dao
from entity import goods


def view():
    print('---------------------')
    print('1 新增商品')
    print('2 展示商品')
    print('3 查找商品')
    print('4 退出')
    print('---------------------')


if __name__ == '__main__':
    while True:
        view()
        chose = input('请输入选择')
        if chose is '1':
            name = input('请输入商品名')
            price = input('请输入价格')
            num = input('请输入数量')
            goods = goods.Goods(name, price, num)
            goods_dao.GoodsDao().add(goods)
            continue
        if chose is '2':
            print(goods_dao.GoodsDao().query_all())
            continue
        if chose is '3':
            name = input('请输入商品名')
            print(goods_dao.GoodsDao().query_by_name(name))
            continue
        if chose is '4':
            break
