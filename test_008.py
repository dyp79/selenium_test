# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/12 16:17
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test_008.py
# @Software: PyCharm

import pytest

# 测试数据
test_datas = [
    {"username": "yoyo1", "password": "123456", "expected": "success!"},
    {"username": "yoyo2", "password": "123456", "expected": "success!"},
    {"username": "yoyo3", "password": "123456", "expected": "success!"},

]


# ids 每条用例的标识，与parames一一对应
@pytest.fixture(params=test_datas, ids=[
    "测试用例1，username：you1",
    "测试用例2，username：yoyo2",
    "测试用例3，username：yoyo3",
])
def login(request):
    """"登录"""
    print(f"\n登录账号:{request.param['username']},密码:{request.param['password']}")
    result = {"code": 0, "msg": "success!"}
    return request.param, result


def test_login(login):
    test_input, result = login
    assert test_input["expected"] == result["msg"]


if __name__ == '__main__':
    pytest.main(["-vs"])
