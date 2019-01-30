# ===========================================================
print('\n测试未通过时怎么办')
# 测试未通过时怎么办呢?如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错。
# 因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码:
    # 检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。

""" 
在这个示例中，get_formatted_name()以前只需要两个实参——名和姓，但现在它要求提供名、中间名和姓。
新增的中间名参数是必不可少的，这导致get_formatted_name()的行为不符合预期。
就这里而言，最佳的选择是让中间名变为可选的。
这样做后，使用类似于Janis Joplin的姓名进行测试时，测试就会通过了，同时这个函数还能接受中间名。
下面来修改get_formatted_name()，将中间名设置为可选的，然后再次运行这个测试用例。
如果通过了，我们接着确认这个函数能够妥善地处理中间名。
"""

import unittest
from name_function import get_formatted_name_three

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name_three('janis', 'joplin')
        print(formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()

"""
在get_formatted_name()的这个新版本中，中间名是可选的。
如果向这个函数传递了中间名 (if middle:)，姓名将包含名、中间名和姓，否则姓名将只包含名和姓。
现在，对于两种不同的姓名，这个函数都应该能够正确地处理。
为确定这个函数依然能够正确地处理像Janis Joplin这样的姓名，我们再次运行test_name_function.py:

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

现在，测试用例通过了。太好了，这意味着这个函数又能正确地处理像Janis Joplin这样的姓名了，而且我们无需手工测试这个函数。
这个函数很容易就修复了，因为未通过的测试让我们得知新代码破坏了函数原来的行为。

"""


