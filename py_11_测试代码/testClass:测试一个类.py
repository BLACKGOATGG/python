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

import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) 

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()

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
