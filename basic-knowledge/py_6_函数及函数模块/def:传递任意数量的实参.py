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

