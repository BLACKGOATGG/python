# ===========================================================
print('测试代码')
# 编写函数或类时，还可为其编写测试。
# 通过测试，可确定代码面对各种输入都能够按要求的那样工作。
# 测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。
# 在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。
# 程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。

# 在本章中
    # 你将学习如何使用Python模块unittest中的工具来测试代码。
    # 你将学习编写测试用例，核实一系列输入都将得到预期的输出。
    # 你将看到测试通过了是什么样子，测试未通过又是什么样子，还将知道测试未通过如何有助于改进代码。
    # 你将学习如何测试函数和类，并将知道该为项目编写多少个测试。


# ===========================================================
print('\n测试函数')
# 要学习测试，得有要测试的代码。
# 下面是一个简单的函数，它接受名和姓并返回整洁的姓名:
from name_function import get_formatted_name

""" print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ") 
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
 """
# 从上述输出可知，合并得到的姓名正确无误。
# 现在假设我们要修改get_formatted_name()，使其还能够处理中间名。
# 这样做时，我们要确保不破坏这个函数处理只有名和姓的姓名的方式。
# 为此，我们可以在每次修改get_formatted_name()后都进行测试:
# 运行程序names.py，并输入像 Janis Joplin这样的姓名，但这太烦琐了。
# 所幸Python提供了一种自动测试函数输出的高效方式。
# 倘若我们对get_formatted_name()进行自动测试，就能始终信心满满，确信给这个函数提供我们测试过的姓名时，它都能正确地工作。


# ===========================================================
print('\n单元测试和测试用例')
# Python标准库中的模块unittest提供了代码测试工具。

# 单元测试用于核实函数的某个方面没有问题;

# 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
# 良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。

# 全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
# 对于大型项目，要实现全覆盖可能很难。
# 通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。


# ===========================================================
print('\n可通过的测试')
# 创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。
# 要为函数编写测试用例，
    # 可先导入模块unittest以及要测试的函数，
    # 再创建一个继承unittest.TestCase的类，
    # 并编写一系列方法对函数行为的不同方面进行测试。

# import unittest
# from name_function import get_formatted_name

# class Name.TestCase(unittest.TestCase):
#     """测试name_function.py"""

#     def test_first_last_name(self):
#         """能够正确地处理像Janis Joplin这样的姓名吗?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()

""" 
首先，我们导入了模块unittest和要测试的函数get_formatted_ name()。
在Ø处，我们创建了一个名为Name.TestCase的类，用于包含一系列针对get_formatted_name()的单元测试。
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


# ===========================================================
print('\n不能通过的测试')
# 测试未通过时结果是什么样的呢?我们来修改get_formatted_name()，使其能够处理中间名，
# 但这样做时，故意让这个函数无法正确地处理像Janis Joplin这样只有名和姓的姓名。
# 下面是函数get_formatted_name()的新版本，它要求通过一个实参指定中间名:

# import unittest
# from name_function import get_formatted_name_two

# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""

#     def test_first_last_name(self):
#         """能够正确地处理像Janis Joplin这样的姓名吗?"""
#         formatted_name = get_formatted_name_two('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()

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

# import unittest
# from name_function import get_formatted_name_three

# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""
#     def test_first_last_name(self):
#         """能够正确地处理像Janis Joplin这样的姓名吗?"""
#         formatted_name = get_formatted_name_three('janis', 'joplin')
#         print(formatted_name)
#         self.assertEqual(formatted_name, 'Janis Joplin')


# unittest.main()

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




