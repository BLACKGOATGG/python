# ===========================================================
print('\n不能通过的测试')
# 测试未通过时结果是什么样的呢?我们来修改get_formatted_name()，使其能够处理中间名，
# 但这样做时，故意让这个函数无法正确地处理像Janis Joplin这样只有名和姓的姓名。
# 下面是函数get_formatted_name()的新版本，它要求通过一个实参指定中间名:
import unittest
from name_function import get_formatted_name_two

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name_two('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

""" 
这个版本应该能够正确地处理包含中间名的姓名，但对其进行测试时，我们发现它再也不能正确地处理只有名和姓的姓名。
这次运行程序test_name_function.py时，输出如下:
    E
    ======================================================================
    ERROR: test_first_last_name (__main__.NamesTestCase)
    能够正确地处理像Janis Joplin这样的姓名吗?
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "test.py", line 126, in test_first_last_name
        formatted_name = get_formatted_name_two('janis', 'joplin')
    TypeError: get_formatted_name_two() missing 1 required positional argument: 'last'

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)

其中包含的信息很多，因为测试未通过时，需要让你知道的事情可能有很多。

第1行输出只 有一个字母E(见Ø)，它指出测试用例中有一个单元测试导致了错误。
接下来，我们看到 NamesTestCase中的test_first_last_name()导致了错误(见)。

测试用例包含众多单元测试时，知道哪个测试未通过至关重要。
在处，我们看到了一个标准的traceback，
它指出函数调用 get_formatted_name('janis', 'joplin')有问题，因为它缺少一个必不可少的位置实参。
我们还看到运行了一个单元测试(见)。
最后，还看到了一条消息，它指出整个测试用例都未通过，因为运行该测试用例时发生了一个错误(见)。
这条消息位于输出末尾，让你一眼就能看到——你可不希望为获悉有多少测试未通过而翻阅长长的输出。

"""


