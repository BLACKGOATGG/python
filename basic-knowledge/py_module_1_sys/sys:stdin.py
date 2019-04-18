import sys

# sys.stdin.readline()
print('Plase input your name: ')
name = sys.stdin.readline()

print('Hello ', name)

# 从上面的小例子可以看出，sys.stdin是一个标准化输入的方法。
# python3中使用sys.stdin.readline()可以实现标准输入，
# 其中默认输入的格式是字符串，如果是int，float类型则需要强制转换。

import sys
try:
    while True:
        print('Please input a number:')
        n = int(sys.stdin.readline().strip('\n')) #strip('\n')表示以\n分隔，否则输出是“字符串+\n”的形式
        print(n)

        print('Please input some numbers:')
        sn = sys.stdin.readline().strip()#若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn == '':
            break
        sn = list(map(int,sn.split())) #如果要强制转换成int等类型，可以调用map()函数。
        print(sn,'\n')
except:
    pass


# python3中sys.stdin与input的区别
# input()方法和stdin()类似，不同的是input()括号内可以直接填写说明文字。
# 可以看一个简单的例子：
while True:
    n = int(input('Please input a number:\n'))
    print(n)

    sn = list(map(int,input('Please input some numbers:\n').split()))
    print(sn,'\n')
    
# 可以看到，input(）和sys.stdin功能基本相同。