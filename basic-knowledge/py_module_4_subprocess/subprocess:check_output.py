import subprocess

# Python3中的subprocess.check_output函数可以执行一条sh命令，并返回命令的输出内容，用法如下：
# 执行命令，并返回执行状态，其中shell参数为False时，命令需要通过列表的方式传入，当shell为True时，可直接传入命令。
"""
output = subprocess.check_output(["python3", "xx.py"], shell = False)

"""

# 该函数两个参数第一个表示命令内容，因为中间有空格所以用中括号这种形式，同时制定shell=False表示命令分开写了。
# 而该命令执行后的输出内容会返回给output变量。
# 需要注意的是这个output变量并不是一个string，也就是说不能用string的一些函数，比如你想知道返回的输出中是否包含某个字符串：
"""
output = subprocess.check_output(["python3", "xx.py"], shell = False)
if (output.find("yes") >= 0): 
    print("yes")
else: 
    print("no")

"""

# 这样执行后不会有任何输出，因为find()函数是给string用的，而这里的output其实不是一个string
# 返回的其实是一个编码后的比特值，实际的编码格式取决于调用的命令，因此python3将解码过程交给应用层，也就是我们使用的人来做。
# 这样就清晰了，要对输出使用stirng的操作，需要先通过解码将其转换成string：
output = subprocess.check_output(["python3", "xx.py"], shell = False)
print(output)
out = output.decode()
print(out)
if (out.find("yes") >= 0):
    print("yes")
else:
    print("no")

# 这样就可以正常判断了。

