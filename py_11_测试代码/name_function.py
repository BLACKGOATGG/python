# 要学习测试，得有要测试的代码。
# 下面是一个简单的函数，它接受名和姓并返回整洁的姓名:

def get_formatted_name(first, last):
    """Generate a neatly formatted full name.""" 
    full_name = first + ' ' + last
    return full_name.title()

# 函数get_formatted_name()将名和姓合并成姓名，在名和姓之间加上一个空格，并将它们的首字母都大写，再返回结果。
# 为核实get_formatted_name()像期望的那样工作，我们来编写一个 使用这个函数的程序。
# 程序names.py让用户输入名和姓，并显示整洁的全名:



def get_formatted_name_two(first, middle, last):
    """生成整洁的姓名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()






