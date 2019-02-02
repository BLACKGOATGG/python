#======================================================
# 标准数据类型

"""
内置的 type() 函数可以用来查询变量所指的对象类型。
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 此外还可以用 isinstance 来判断：
a = 111
print(isinstance(a, int))

""" 
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。

注意：
    在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
    到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
"""




