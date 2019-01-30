# ===========================================================
print('\n使用json.dump()和json.load()')
# 我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
# 第一个程序将使用json.dump()来存储这组数字，而第二个程序将使用json.load()。
# 函数json.dump()接受两个实参: 要存储的数据以及可用于存储数据的文件对象。
# 函数json.dump()接受一个实参: 用于存储数据的文件对象。
#注意，文件名不能用json，会导致python优先读取该‘json’文件导致代码出错
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
print(1)
with open(filename, 'w') as f_obj:
    print(2)
    print(numbers)
    json.dump(numbers, f_obj)
    numbers = ''
    print(3)
print(4)

with open(filename) as f_obj:
    print(5)
    print(numbers)
    numbers = json.load(f_obj)

print(6)    
print(numbers)
# 这是一种在程序之间共享数据的简单方式。
# 以上代码非异步

