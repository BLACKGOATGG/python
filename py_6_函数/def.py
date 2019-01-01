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

# ===========================================================
print('\n实参和形参')
# 在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
# 在代码greet_user('gjl')中，值'gjl'是一个实参。实参是调用函数时传递给函数的信息。
# 我们调用函数时，将要让函数使用的信息放在括号内。
# 在greet_user('gjl')中，将实参'gjl'传递给了函数greet_user()，这个值被存储在形参username中。

# 传递实参
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参 的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;
# 也可使用关键字实参，其中每个实参都由变量名和值组成;还可使用列表和字典。

def describe_pet(animal_type='null', pet_name='null'): 
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


print('\n位置实参')
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
# 位置实参的顺序很重要,使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料
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


# ===========================================================
print('\n返回值')
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
# 在函数中，可使用return语句将值返回到调用函数的代码行。
# 返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
def get_formatted_name(first_name, last_name , middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

aaa = get_formatted_name('AAA', 'aa', 'middle')
bbb = get_formatted_name('BBB', 'bb')
ccc = get_formatted_name('CCC', 'cc', 'middle')
print(aaa)
print(bbb)
print(ccc)

# 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name , middle_name='' , age =''):
    person = {
        'first_name':first_name.title(),
        'last_name':last_name.title()
    }
    if middle_name:
        person['middle_name'] = middle_name.title()
    if age:
        person['age'] = age
    return person
            
ddd = build_person('DDD', 'dd', 'middle')
eee = build_person('EEE', 'ee')
fff = build_person('FFF', 'ff',age='18',middle_name='hhh')
print(ddd)
print(eee)
print(fff)

# while True:
#     print("\nPlease tell me your name:") 
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     m_name = input("Middle name: ")
#     if m_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name ,m_name) 
#     print("\nHello, " + formatted_name + "!")


# ===========================================================
print('\n传递列表')
# 经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象(如字典)。
# 将列表传递给函数后，函数就能直接访问其内容。
def greet_users(names): 
    """向列表中的每位用户都发出简单的问候""" 
    for name in names:
        msg = "Hello, " + name.title() + "!" 
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


print('\n在函数中修改列表')
# 将列表传递给函数后，函数就可对其进行修改。
# 在函数中对这个列表所做的任何修改都是永久性的，这能够高效地处理大量的数据。
def print_models(unprinted_designs, completed_models): 
    """模拟打印每个设计，直到没有未打印的设计为止打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models): 
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print(unprinted_designs)


print('\n禁止函数修改列表')
# 有时候，需要禁止函数修改列表。
# 为解决这个问题，可向函数传递列表的副本而不是原件;
# 这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
# 切片表示法[:]创建列表的副本。

unprinted_designs_two = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models_two = []

print_models(unprinted_designs_two[:],completed_models_two)
show_completed_models(completed_models_two)

print(unprinted_designs_two)


# ===========================================================
print('\n传递任意数量的实参')
# 有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
def make_pizza(*toppings): 
    """打印顾客点的所有配料""" 
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


print('\n结合使用位置实参和任意数量实参')
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza_two(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_two(16, 'pepperoni')
make_pizza_two(12, 'mushrooms', 'green peppers', 'extra cheese')


print('\n使用任意数量的关键字实参')
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')
print(user_profile)


