# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/2 15:36
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test02.py
# @Software: PyCharm
all_name = ['v_ccongyang', 'v_dahaochen', 'v_dalishao', 'v_ipanwang', 'v_iwbzhang', 'v_junywen',
            'v_kmingzou', 'v_lixuanli', 'v_whuahuang', 'v_yanpdu', 'v_zyni']
for i in all_name:
    new_name = i[2::]
    if new_name == 'yanpdu':
        print(new_name+':是我的名字')
    else:
        print(new_name+':不是我的名字')
