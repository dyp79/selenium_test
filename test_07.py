# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/11 15:04
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test_07.py
# @Software: PyCharm
# 输入日期判断是否是工作日
import datetime

import pytest
from v_yanpdu.WhatTime import what_time


# 整个模块运行前面输出
def setup_module():
    print("-----module-test-being--------")


# 模块运行后输出
def teardown_module():
    print("-----module-test-end--------")


# 函数式
def setup_function():
    print('setup_function:每个用例前都会执行')


def teardown_function():
    print('teardown_function:每个用例后都会执行')


def test_function():
    print("----这是一个不在类里面的方法-----")


class Test_07:
    # 类前运行输出
    def setup_class(self):
        print("-----class-test-being--------")

    # 类后运行输出
    def teardown_class(self):
        print("-----class-test-end--------")

    # 方法前运行输出
    def setup_method(self):
        print("-----method-test-being--------")

    # 方法后运行输出
    def teardown_method(self):
        print("-----method-test-end--------")

    # 方法调用前输出
    def setup(self):
        print("-----class-run-test-being--------")

    # 方法调用后输出
    def teardown(self):
        print("--------class-run-test-end--------")

    def test_WhatTime(self):
        test_time = int(input("请输入工作日期："))
        today = what_time(test_time)
        print(today)

    @pytest.mark.run_this_case
    def test_WhatTime2(self):
        print("-----指定运行-----")
        today = datetime.datetime.now().weekday() + 1
        print("今天是周"+str(today))


# if __name__ == '__main__':
#     pytest.main(["-vs"])
