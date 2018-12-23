# ===========================================================
print('函数')
# 函数让你能够将程序分成多个很小的部分，其中每部分都负责完成一项具体任务。
# 你可以根据需要调用同一个函数任意次，还可将函数存储在独立的文件中。
# 使用函数可让你编写的代码效率更高，更容易维护和排除故障，还可在众多不同的程序中重用。


print('\n定义函数')
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")

n = 0
while n<3:
    n += 1
    greet_user('gjl'+str(n))

# 实参和形参
# 在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
# 在代码greet_user('gjl')中，值'gjl'是一个实参。实参是调用函数时传递给函数的信息。
# 我们调用函数时，将要让函数使用的信息放在括号内。
# 在greet_user('gjl')中，将实参'gjl'传递给了函数greet_user()，这个值被存储在形参username中。

# 传递实参
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参 的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;
# 也可使用关键字实参，其中每个实参都由变量名和值组成;还可使用列表和字典。


print('\n位置实参')
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
# 位置实参的顺序很重要,使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料
def describe_pet(animal_type='null', pet_name='null'): 
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('cat', 'jiafei')


print('\n关键字实参')
# 关键字实参是传递给函数的名称—值对,直接在实参中将名称和值关联起来了
# 因此向函数传递实参时不会混淆(不会得到名为Hamster的harry这样的结果)。
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
describe_pet(animal_type='cat', pet_name='jiafei')


print('\n默认值')
# 编写函数时，可给每个形参指定默认值。
# 在调用函数中给形参提供了实参时，Python将使用指定的实参值;否则，将使用形参的默认值。
# 因此，给形参指定默认值后，可在函数调用中省略相应的实参。
# 使用默认值可简化函数
# 调用，还可清楚地指出函数的典型用法。
describe_pet('true')
describe_pet(animal_type = 'true')
describe_pet(pet_name = 'true')
describe_pet()



