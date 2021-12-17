# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/14 20:08
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test04_read.py
# @Software: PyCharm
import csv
import shutil


def test_csv_read():
    # 读取unsort.csv文件并将指定数据写入文件中
    with open('unsort.csv', 'r', encoding='utf-8')as f:
        # 生成reader对象
        lines = csv.reader(f)
        lines = list(lines)
        for line in lines:
            print(f"{line[0]},{line[1]},{line[4]},{line[5]},{line[7]}")
            # 方法一：写入到csv中
            # with open("test.csv", "a", encoding='utf-8') as f2:
            #     生成writer对象
            #     writer = csv.writer(f2)
            #     writer.writerows([[line[0], line[1], line[4], line[5], line[7]]])
            # 方法二：写入到txt中
            with open('./sort.txt', 'a', encoding='utf-8') as f1:
                f1.write(line[0]), f1.write(line[1]), f1.write(line[4]), f1.write(line[5]), f1.write(line[7]), f1.write("\n")
                f1.close()


def test_shutil():
    # 移动sort.txt文件
    shutil.move('./sort.txt', 'F:/pc-work3/')


if __name__ == '__main__':
    test_csv_read()
    # test_shutil()
