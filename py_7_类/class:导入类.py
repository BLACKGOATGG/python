# ===========================================================
print('\n导入类')
# 随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。
# 为遵循Python的总体理念，应让文件尽可能整洁。
# 为在这方面提供帮助，Python允许你将类存储在模块中，然后在主程序中导入所需的模块。

print('\n导入单个类')
# 导入类是一种有效的编程方式。如果在这个程序中包含了整个Car类，它该有多长呀!
# 通过将这个类移到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文件变得整洁而易于阅读了。
# 这还能让你将大部分逻辑存储在独立的文件中;确定类像你希望的那样工作后，你就可以不管这些文件，而专注于主程序的高级逻辑了。

# from car import Car
# 调用方法：Car()


print('\n从一个模块中导入多个类')
# 可根据需要在程序文件中导入任意数量的类。

# from car import Car, ElectricCar
# 调用方法：Car()   or  ElectricCar()


print('\n导入整个模块')
# 你还可以导入整个模块，再使用句点表示法访问需要的类。
# 这种导入方法很简单，代码也易于阅读。
# 由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。

# import car
# 调用方法：car.Car()   or  car.ElectricCar()   or  cer.Battery()


print('\n导入模块中的所有类')
# 不推荐使用这种导入方式，其原因有二。
    # 1. 首先，如果只要看一下文件开头的import语句，就能清楚地知道程序使用了哪些类，将大有裨益;
    # 但这种导入方式没有明确地指出你使用了模块中的哪些类。
    # 2. 这种导入方式还可能引发名称方面的困惑。
    # 如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
# 需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法来访问类。(也就是方法三)
    # 1. 这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地方使用了导入的模块;
    # 2. 你还避免了导入模块中的每个类可能引发的名称冲突。
# 这里之所以介绍这种导入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。

# from car import *
# 调用方法：Car()   or  ElectricCar()   or  Battery()

print('\n在一个模块中导入另一个模块')
# 有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
# 将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。
# 在这种情况下，可在前一个模块中导入必要的类。
# ！！！！！！！！！！！！！！！！！（此处未实践）！！！！！！！！！！！！！！！！！！！！！！！


from car import Car,ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name()) 

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_tesla = ElectricCar('tesla', 'models', 2016)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


