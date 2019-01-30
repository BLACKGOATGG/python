# ===========================================================
print('\n测试函数')
# 要学习测试，得有要测试的代码。
# 下面是一个简单的函数，它接受名和姓并返回整洁的姓名:
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ") 
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

# 从上述输出可知，合并得到的姓名正确无误。
# 现在假设我们要修改get_formatted_name()，使其还能够处理中间名。
# 这样做时，我们要确保不破坏这个函数处理只有名和姓的姓名的方式。
# 为此，我们可以在每次修改get_formatted_name()后都进行测试:
# 运行程序names.py，并输入像 Janis Joplin这样的姓名，但这太烦琐了。
# 所幸Python提供了一种自动测试函数输出的高效方式。
# 倘若我们对get_formatted_name()进行自动测试，就能始终信心满满，确信给这个函数提供我们测试过的姓名时，它都能正确地工作。

