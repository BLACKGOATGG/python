# ===========================================================
print('\n可通过的测试')
# 创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。
# 要为函数编写测试用例，
    # 可先导入模块unittest以及要测试的函数，
    # 再创建一个继承unittest.TestCase的类，
    # 并编写一系列方法对函数行为的不同方面进行测试。
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

""" 
首先，我们导入了模块unittest和要测试的函数get_formatted_ name()。
在Ø处，我们创建了一个名为NamesTestCase的类，用于包含一系列针对get_formatted_name()的单元测试。
你可随便给这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。
这个类必须继承 unittest.TestCase类，这样Python才知道如何运行你编写的测试。

NamesTestCase 只包含一个方法，用于测试get_formatted_name()的一个方面。
我们将这个方法命名为test_first_last_name()，因为我们要核实的是只有名和姓的姓名能否被正确地格式化。
我们运行test_name_function.py时，所有以test_打头的方法都将自动运行。
在这个方法中，我们调用了要测试的函数，并存储了要测试的返回值。
在这个示例中，我们使用实参'janis'和'joplin' 调用get_formatted_name()，并将结果存储到变量formatted_name中(见)。

在处，我们使用了unittest类最有用的功能之一:
    一个断言方法。 断言方法用来核实得到的结果是否与期望的结果一致。
    在这里，我们知道get_formatted_name()应返回这样的姓名，即名和姓的首字母为大写，且它们之间有一个空格，
    因此我们期望formatted_name的值为Janis Joplin。
    为检查是否确实如此，我们调用 unittest 的方法 assertEqual()，并向它传递formatted_ name和'Janis Joplin'。

    代码行self.assertEqual(formatted_name, 'Janis Joplin')的意思是说:
        “将formatted_name的值同字符串'Janis Joplin'进行比较，如果它们相等，就万事大吉，如果它 们不相等，跟我说一声!”

代码行unittest.main()让Python运行这个文件中的测试。运行test_name_function.py时，得 到的输出如下:

. 
----------------------------------------------------------------------
Ran 1 test in 0.000s
            OK

第1行的句点表明有一个测试通过了。
接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒。
最后的OK表明该测试用例中的所有单元测试都通过了。

上述输出表明，给定包含名和姓的姓名时，函数get_formatted_name()总是能正确地处理。
修改get_formatted_name()后，可再次运行这个测试用例。
如果它通过了，我们就知道在给定Janis Joplin这样的姓名时，这个函数依然能够正确地处理。

 """


