# ===========================================================
print('\n添加新测试')
# 确定get_formatted_name()又能正确地处理简单的姓名后，我们再编写一个测试，用于测试包含中间名的姓名。
# 为此，我们在NamesTestCase类中再添加一个方法:

import unittest
from name_function import get_formatted_name_three

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name_three('janis', 'joplin')
        print(formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
        formatted_name = get_formatted_name_three('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()

""" 
我们将这个方法命名为test_first_last_middle_name()。
方法名必须以test_打头，这样它才会在我们运行test_name_function.py时自动运行。
这个方法名清楚地指出了它测试的是get_ formatted_name()的哪个行为，这样，如果该测试未通过，我们就会马上知道受影响的是哪种类型的姓名。

在TestCase类中使用很长的方法名是可以的;
这些方法的名称必须是描述性的，这才能让你明白测试未通过时的输出;
这些方法由Python自动调用，你根本不用编写调用它们的代码。

为测试函数get_formatted_name()，我们使用名、姓和中间名调用它(见Ø)，
再使用assertEqual()检查返回的姓名是否与预期的姓名(名、中间名和姓)一致。
我们再次运行 test_name_function.py时，两个测试都通过了:

    .
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    OK

太好了!现在我们知道，这个函数又能正确地处理像Janis Joplin这样的姓名了，
我们还深信它也能够正确地处理像Wolfgang Amadeus Mozart这样的姓名。
"""


