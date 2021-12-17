# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/18 18:56
# @Author : v_yanpdu
# @Email : lanlan_bupt@126.com
# @File : test05.py
# @Software: PyCharm
# class TestExcept:
#     """
#     try...expect使用
#     repr()  将返回的object----string
#     """
#
#     def test01(self):
#         """except异常"""
#         a = "aa"
#         b = 1.5
#         try:
#             sum = a * b
#             print(sum)
#         except:
#             print("-------test01 error--------")
#
#     def test02(self):
#         """整数数值类型错误, ValueError异常"""
#         """事实上，raise 语句引发的异常通常用 try except（else finally）异常处理结构来捕获并进行处理"""
#         try:
#             a = 0.1
#             if not a.is_integer():
#                 raise ValueError("a必须是整数")
#         except ValueError as e:
#             print("This error is:", e)
#
#     def test03(self):
#         """异常和非异常的情况处理"""
#         try:
#             print("-----test03 execute-----")
#         except Exception as e:
#             print("This error is:", str(e))
#         else:
#             print("-----test03 not hava error-----")
#
#     def test04(self):
#         """是否发生异常都执行最后的finally"""
#         try:
#             print("-----test04 execute-----")
#         finally:
#             print("This is finally")
#
#     def test05(self):
#         """返回错误明细"""
#         a = 0
#         b = 5
#         try:
#             c = b / a
#             print(c)
#         except ZeroDivisionError as e:
#             # print("This error is:", repr(e))
#             print("This error is:", e.args)
#
#     def test06(self):
#         """try里面使用raise抛出了IndexError 异常，程序会跳转到except子句中执行
#             输出打印语句，然后使用raise再次引发刚刚发生的异常，导致程序出现错误而终止运行"""
#         try:
#             raise IndexError
#
#         except:
#             print("出错了")
#             raise
#
#
# if __name__ == '__main__':
#     # TestExcept().test01()
#     # TestExcept().test02()
#     # TestExcept().test03()
#     # TestExcept().test04()
#     # TestExcept().test05()
#     TestExcept().test06()
#
import traceback
import sys


class SelfException(Exception):
    '''
     traceback异常的传播轨迹，追踪异常触发的源头
     sys.exc_info(type,value,traceback)将异常信息以元组形式返回
        type：异常类型的名称，它是 BaseException 的子类
        value：捕获到的异常实例。
        traceback：是一个 traceback 对象。

    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    '''
    pass

    def main(self):
        self.firstMethod()

    def firstMethod(self):
        self.secondMethod()

    def secondMethod(self):
        self.thirdMethod()

    def thirdMethod(self):
        raise SelfException("自定义异常信息")


if __name__ == '__main__':
    try:
        SelfException().main()
    except:
        # 捕捉异常，并将异常传播信息输出控制台 traceback.print_exc() # 捕捉异常，并将异常传播信息输出指定文件中
        traceback.print_exc(file=open('log.txt', 'a'))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print('以下为代码错误信息:')
        print('exc_type(异常类型): {}\nexc_value(异常错误的信息): {}\nexc_traceback(调用堆栈封装在最初发生异常的地方): {}'.format(exc_type,
                                                                                                       exc_value,
                                                                                                       exc_traceback))
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        traceback.print_tb(exc_traceback, limit=None, file=open('log.log', mode='a', encoding='utf-8'))
        # exc_traceback 调用堆栈封装在最初发生异常的地方
        # limit= 此处显示需要显示的回溯的层级，设定为None则显示所有层级，设置为1，则显示最初一层 可以设置回溯层级比错误层级高的数
        # file=sys.stdout:此为在控制台输出错误信息，file=open('log.log', mode='a', encoding='utf-8')存储于文件中
