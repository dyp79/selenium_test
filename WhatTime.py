# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/12 15:05
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : WhatTime.py
# @Software: PyCharm
import pytest


def what_time(test_time):
    try:
        if 0 < test_time < 6:
            return "今天是工作日"
        elif 5 < test_time < 8:
            return "今日休息"
        else:
            return f"当前输入是：{test_time},一周只有7天，请输入1-7"
    except:
        return f"当前输入是：{test_time},请检查输入是否正确，只能输入1-7，周日用7代替"
