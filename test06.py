# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/22 14:58
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test06.py
# @Software: PyCharm
import requests


class Test_Request:
    """ 在app内分别抓取http协议get和post的请求，用requests调通"""

    def test_GetRequest(self):
        """获取TVK后台无极配置信息"""
        url = "https://appcfg.v.qq.com/getconf"
        params = {"cmd": "tvk_sdk_config",
                "random": "0.21901299481411185",
                "subver_two": "V_29",
                "dev": "V1924A",
                "name": "000",
                "guid": "f62b6f32318311ec89cd6c92bf48bcb2",
                "platform": "aphone",
                "subver": "V_9.36.000.1136"
                }
        response = requests.get(url, params=params)
        print(response.text)
        print(response.status_code)

    def test_PostRequest(self):
        """获取启动信息(ip，启动时间戳等)"""
        url = "https://vv.video.qq.com/checktime"
        data = {"randnum": "0.8805924396656467",
                "guid": "f62b6f32318311ec89cd6c92bf48bcb2",
                "otype": "json"
                }
        response = requests.post(url, data=data)
        print(response.text)
        print(response.status_code)


if __name__ == "__main__":
    Test_Request().test_GetRequest()
    Test_Request().test_PostRequest()
