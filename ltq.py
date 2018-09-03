# -*- coding: UTF-8 -*-
# # 制作一个"密码薄",其可以存储一个网址（例如 www.itcast.cn），和一个密码(例如 123456)，
# 请编写程序完成这个“密码薄”的增删改查功能，并且实现文件存储功能
import ast
import os

while True:
    print("---------密码薄---------")
    print("1.增加一个网址跟密码")
    print("2.删除一个网址跟密码")
    print("3.更改一个网址跟密码")
    print("4.查找一个网址跟密码")
    print("0.退出密码薄")
    print("------------------------")
    CheckNum = int(input("请输入功能对应的数字码"))
    if CheckNum == 1:
        dict = {}
        f = open("d.txt", "a")
        # WebSiteName = input("请输入您的网址:")
        # PassWordName = input("请输入您的密码:")
        # dict['website'] = str(WebSiteName)
        # dict['password'] = str(PassWordName)
        # dictstr = str(dict)
        # f.write(dictstr+"\n")
        WebSiteName = input("请输入您的网址:")
        PassWordName = input("请输入您的密码:")
        dict['website'] = WebSiteName
        dict['password'] = PassWordName
        dictstr = str(dict)
        f.write(dictstr+"\n")
        print("添加成功")
        f.close()
    if CheckNum == 2:
        q = 0
        WebSiteName = input("请输入要删除的网址:")
        f = open("d.txt", 'r+')
        s = open("d.txt", 'a')
        list = f.readlines()
        f.seek(0)
        f.truncate()
        for i in list:
            q += 1
            strs = i.split("\n")
            strdict = ast.literal_eval((strs[0]))
            if WebSiteName == strdict['website']:
                print("删除成功")
                q -= 1
            else:
                if q == len(list):
                    print("未找到该网址")
                s.write(i)
        f.close()
        s.close()
    if CheckNum == 3:
        q = 0
        WebSiteName = input("请输入要修改的网址:")
        f = open("d.txt", 'r+')
        s = open("d.txt", 'a')
        list = f.readlines()
        f.seek(0)
        f.truncate()
        for i in list:
            q += 1
            strs = i.split("\n")
            strdict = ast.literal_eval((strs[0]))
            if WebSiteName == strdict['website']:
                editname = input("请输入修改的网址:")
                editpasswordName = input("请输入修改的密码:")
                strdict['website'] = editname
                strdict['password'] = editpasswordName
                s.write(str(strdict)+"\n")
                print("修改成功")
                q -= 1
            else:
                if q == len(list):
                    print("未找到该网址")
                s.write(i)
        f.close()
        s.close()
    if CheckNum == 4:
        i = 0
        WebSiteName = input("请输入要修改的网址:")
        f = open("d.txt", "r")
        list = f.readlines()
        for str in list:
            i += 1
            strs = str.split("\n")
            strdict = ast.literal_eval(strs[0])
            if WebSiteName == strdict['website']:
                print("网址：%s,密码:%s" %
                      (strdict['website'], strdict['password']))
                i -= 1
                break
            else:
                if i == len(list):
                    print("未找到该网址")
    if CheckNum == 0:
        break
