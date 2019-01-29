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