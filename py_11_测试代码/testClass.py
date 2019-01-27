# ===========================================================
print('测试类')
""" 
在本章前半部分，你编写了针对单个函数的测试，下面来编写针对类的测试。
很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。
如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。
"""


# ===========================================================
print('\n各种断言方法')
"""
Python在unittest.TestCase类中提供了很多断言方法。
前面说过，断言方法检查你认为应该满足的条件是否确实满足。
如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
如果你认为应该满足的条件实际上并不满足，Python将引发异常。

表11-1描述了6个常用的断言方法。
使用这些方法可核实返回的值等于或不等于预期的值、返回的值为True或False、返回的值在列表中或不在列表中。
你只能在继承unittest.TestCase的类中使用这些方法，下面来看看如何在测试类时使用其中的一个。

                  表11-1 unittest Module中的断言方法
                方法                            用途
            assertEqual(a, b)               核实a == b
            assertNotEqual(a, b)            核实a != b
            assertTrue(x)                   核实x为True
            assertFalse(x)                  核实x为False
            assertIn(item, list)            核实item在list中
            assertNotIn(item, list)         核实item不在list中

"""


# ===========================================================
print('\n一个要测试的类')
# 类的测试与函数的测试相似 —— 你所做的大部分工作都是测试类中方法的行为，但存在一些不同之处，
# 下面来编写一个类进行测试。
# 来看一个帮助管理匿名调查的类:

""" 
这个类首先存储了一个你指定的调查问题(见Ø)，并创建了一个空列表，用于存储答案。
这个类包含打印调查问题的方法(见)、
在答案列表中添加新答案的方法(见)
以及将存储在列表中的答案都打印出来的方法(见)。
要创建这个类的实例，只需提供一个问题即可。

有了表示调查的实例后，
就可使用show_question()来显示其中的问题，
可使用store_response()来存储答案，
并使用show_results()来显示调查结果。

"""
# 为证明AnonymousSurvey类能够正确地工作，我们来编写一个使用它的程序:

from survey import AnonymousSurvey

""" #定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results() """

"""
AnonymousSurvey类可用于进行简单的匿名调查。
假设我们将它放在了模块survey中，并想进行改进:
    让每位用户都可输入多个答案;
    编写一个方法，它只列出不同的答案，并指出每个答案出现了多少次;
    再编写一个类，用于管理非匿名调查。

进行上述修改存在风险，可能会影响AnonymousSurvey类的当前行为。
    例如，允许每位用户输入多个答案时，可能不小心修改了处理单个答案的方式。
    要确认在开发这个模块时没有破坏既有行为，可以编写针对这个类的测试。

"""


# ===========================================================
print('\n测试AnonymousSurvey类')
# 下面来编写一个测试，对AnonymousSurvey类的行为的一个方面进行验证:
    # 如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。
    # 为此，我们将在这个答案被存储后，使用方法assertIn()来核实它包含在答案列表中:

# import unittest
# from survey import AnonymousSurvey

# class TestAnonmyousSurvey(unittest.TestCase):
#     """针对AnonymousSurvey类的测试"""
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn('English', my_survey.responses) 

# unittest.main()

""" 
我们首先导入了模块unittest以及要测试的类AnonymousSurvey。
我们将测试用例命名为 TestAnonymousSurvey，它也继承了unittest.TestCase(见Ø)。
第一个测试方法验证调查问题的单个答案被存储后，会包含在调查结果列表中。
对于这个方法，一个不错的描述性名称是 test_store_single_response()(见)。
如果这个测试未通过，我们就能通过输出中的方法名得知，在存储单个调查答案方面存在问题。
要测试类的行为，需要创建其实例。

在处，我们使用问题"What language did you first learn to speak?"创建了一个名为my_survey的实例，
然后使用方法store_response()存储了单个答案 English。
接下来，我们检查English是否包含在列表my_survey.responses中，以核实这个答案是 否被妥善地存储了(见)。
当我们运行test_survey.py时，测试通过了: 

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

这很好，但只能收集一个答案的调查用途不大。
下面来核实用户提供三个答案时，它们也将被妥善地存储。
为此，我们在TestAnonymousSurvey中再添加一个方法:

"""

# import unittest
# from survey import AnonymousSurvey

# class TestAnonmyousSurvey(unittest.TestCase):
#     """针对AnonymousSurvey类的测试"""
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn('English', my_survey.responses) 

#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?" 
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)

#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# unittest.main()

""" 
我们将这个方法命名为test_store_three_responses()，并像test_store_single_response() 一样，在其中创建一个调查对象。
我们定义了一个包含三个不同答案的列表(见Ø)，再对其中每个答案都调用store_response()。
存储这些答案后，我们使用一个循环来确认每个答案都包含在my_survey.responses中(见)。
我们再次运行test_survey.py时，两个测试(针对单个答案的测试和针对三个答案的测试)都 通过了:

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

前述做法的效果很好，但这些测试有些重复的地方。下面使用unittest的另一项功能来提高它们的效率。

"""


# ===========================================================
print('\n方法setUp()')
# 在前面的test_survey.py中，我们在每个测试方法中都创建了一个AnonymousSurvey实例，并在每个方法中都创建了答案。
# unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。
# 如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
# 这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。

""" 
下面使用setUp()来创建一个调查对象和一组答案，供方法test_store_single_response()和 test_store_three_responses()使用:
"""
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

"""
方法setUp()做了两件事情:
    创建一个调查对象(见Ø);
    创建一个答案列表(见)。
存储这两样东西的变量名包含前缀self(即存储在属性中)，因此可在这个类的任何地方使用。
这让两个测试方法都更简单，因为它们都不用创建调查对象和答案。

方法test_store_three_response() 核实self.responses中的第一个答案——self.responses[0]——被妥善地存储，
而方法test_store_three_response()核实self.responses中的全部三个答案都被妥善地存储。

再次运行test_survey.py时，这两个测试也都通过了。
如果要扩展AnonymousSurvey，使其允许每位用户输入多个答案，这些测试将很有用。
修改代码以接受多个答案后，可运行这些测试，确认存储单个答案或一系列答案的行为未受影响。

测试自己编写的类时，方法setUp()让测试方法编写起来更容易:
可在setUp()方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。
相比于在每个测试方法中都创建实例并设置其属性，这要容易得多。

# 注意
运行测试用例时，每完成一个单元测试，Python都打印一个字符:
测试通过时打印一个句点;
测试引发错误时打印一个E;
测试导致断言失败时打印一个F。

这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。
如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了。

"""


