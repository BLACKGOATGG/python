# -*- coding: UTF-8 -*-
hello = "hello world!"
print(hello)

a = ['cat', 'window', 'defenestrate']
arr = []

#同js的for in循环
# for x in a:
#     print(x, len(x))

# make a slice copy of the entire list 对整个列表做一个切片的拷贝
# for x in a[:]: 
#     if len(x) > 6: a.insert(0, x)
# print(a)

# range()方法生成一个等差级数链表
# 配合这个方法可以实现for循环
# for i in range(5):
#     print(i)

# 在不同方面 range() 函数返回的对象表现为它是一个列表，但事实上它并不是。 当
# 你迭代它时，它是一个能够像期望的序列返回连续项的对象；但为了节省空间，它并
# 不真正构造列表。
# print(range(10))

# 我们称此类对象是 可迭代的 ，即适合作为那些期望从某些东西中获得连续项直到结束
# 的函数或结构的一个目标（参数）。 我们已经见过的 for 语句就是这样一个 迭代器。
# list() 函数是另外一个（ 迭代器），它从可迭代（对象）中创建列表
# print(list(range(5)))

# break 语句和 C 中的类似，用于跳出最近的一级 for 或 while 循环。
# 循环可以有一个 else 子句；它在循环迭代完整个列表（对于 for ）或执行条件为
# false （对于 while ）时执行，但循环被 break 中止的情况下不会执行。
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         print(n, '是一个素数')

# continue 语句是从 C 中借鉴来的，它表示循环继续执行下一次迭代:
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("发现一个偶数", num)
#         continue
#     print("发现一个奇数", num)

# 关键字 def 引入了一个函数 定义 。在其后必须跟有函数名和包括形式参数的圆括号。
# 函数体语句从下一行开始，必须是缩进的。
# 函数体的第一行语句可以是可选的字符串文本，这个字符串是函数的文档字符串，或
# 者称为 docstring 。 有些工具通过docstrings 自动生成在线的或可打印的文档，
# 或者让用户通过代码交互浏览；在你的代码中包含 docstrings 是一个好的实践，
# 让它成为习惯吧。
# def fibonacci(n):
#     """将一个斐波那契的级数打印到n。"""
#     a,b=0,1
#     while b<n:
#         # print(b,end=' ')
#         arr.insert(len(arr),b)
#         a,b=b,a+b
#     print(arr)

# fibonacci(200)


# print hello.decode("utf-8").encode("gbk");
