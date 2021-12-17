# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/2 16:45
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test03_random.py
# @Software: PyCharm
import random
import uuid
import string


class test03_random:
    def test_random_int(self, n):
        # 生成n个20-50之间的随机数
        for i in range(0, n):
            print(random.randint(20, 50))

    def test_yzm1(self):
        # 生成4位整数数验证码
        print(random.randint(1000, 10000))

    def test_yzm2(self):
        # 生成4位字符串以及数字组和验证码
        number = string.digits + string.ascii_letters
        print(''.join(random.sample(number, 4)))

    def test_uuid(self):
        # 生成100个20位激活码
        # 12345-12345-12345-12345
        for i in range(1, 101):
            # 1、使用uuid随机生成32位随机码
            uuid_number = str(uuid.uuid4())
            # 2、去除“-”
            uuid_number = uuid_number.replace('-', '')
            # 生成20位，每5位加“-”
            uuid_num_list = list(uuid_number[0:20])
            for j in range(0, 23):
                if j == 5 or j == 11 or j == 17:
                    uuid_num_list.insert(j, '-')
            uuid_num_list = ''.join(uuid_num_list)
            print(f'第{i}个激活码：{uuid_num_list}')


if __name__ == '__main__':
    # test03_random().test_random_int(5)
    # test03_random().test_yzm1()
    # test03_random().test_yzm2()
    test03_random().test_uuid()

