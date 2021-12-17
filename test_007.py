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

test_data = [{"weekday": "星期一", "waittime": 1},
             {"weekday": "星期二", "waittime": 2},
             {"weekday": "星期三", "waittime": 3},
             {"weekday": "星期四", "waittime": 4},
             {"weekday": "星期五", "waittime": 5},
             {"weekday": "星期六", "waittime": 6},
             {"weekday": "星期日", "waittime": 7}]


@pytest.fixture(params=test_data, ids=["test1", "test2", "test3", "test4", "test5", "test6", "test7"])
def what_time(request):
    try:
        if 0 < request.param['waittime'] < 6:
            return f"今天是{request.param['weekday']},今天是工作日"
        elif 5 < request.param['waittime'] < 8:
            return f"今天是{request.param['weekday']},今日休息"
    except Exception as e:
        return "当前错误是：" + e


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

    def test_WhatTime(self, what_time):
        result = what_time
        print(result)


if __name__ == '__main__':
    pytest.main(["-vs"])
