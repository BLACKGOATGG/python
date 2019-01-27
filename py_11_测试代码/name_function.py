# 要学习测试，得有要测试的代码。
# 下面是一个简单的函数，它接受名和姓并返回整洁的姓名:

def get_formatted_name(first, last):
    """Generate a neatly formatted full name.""" 
    full_name = first + ' ' + last
    return full_name.title()

# 函数get_formatted_name()将名和姓合并成姓名，在名和姓之间加上一个空格，并将它们的首字母都大写，再返回结果。
# 为核实get_formatted_name()像期望的那样工作，我们来编写一个 使用这个函数的程序。
# 程序names.py让用户输入名和姓，并显示整洁的全名:


# 下面是函数get_formatted_name()的新版本，它要求通过一个实参指定中间名:
def get_formatted_name_two(first, middle, last):
    """生成整洁的姓名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()


# 要将中间名设置为可选的，可在函数定义中将形参middle移到形参列表末尾，并将其默认值指定为一个空字符串。
# 我们还要添加一个if测试，以便根据是否提供了中间名相应地创建姓名:
def get_formatted_name_three(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()







