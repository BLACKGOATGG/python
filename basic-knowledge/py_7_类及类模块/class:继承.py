# ===========================================================
print('\n继承')
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;
# 原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止将里程表读数往回调
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """汽车油箱"""
        print("汽车油箱!")

my_new_car = Car('audi', 'a4', 2016)

class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性""" 
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('特斯拉', 'models', 2016)
print(my_tesla.get_descriptive_name())

# 子类的方法__init__()
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。
# 为此，子类的方法__init__()需要父类施以援手。

# 创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 定义子类时，必须在括号内指定父类的名称。

# super()是一个特殊函数，帮助Python将父类和子类关联起来。
# 这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性。
# 父类也称为超 类(superclass)，名称super因此而得名。


print('\n给子类定义属性和方法')
# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。
my_tesla.battery.describe_battery()


print('\n重写父类的方法')
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
# 为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
# 这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
my_tesla.fill_gas_tank()
my_new_car.fill_gas_tank()

# 使用继承时，可让子类保留从父类那里继承而来的精华， 并剔除不需要的糟粕。


print('\n将实例用作属性')
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多:属性和方法清单以及文件都越来越长。
# 在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
# 你可以将大型类拆分成多个协同工作的小类。
my_tesla.battery.get_range()


print('\n模拟实物')
# 模拟较复杂的物件(如电动汽车)时，需要解决一些有趣的问题。
# 续航里程是电瓶的属性还是汽车的属性呢?
    # 如果我们只需描述一辆汽车，那么将方法get_range()放在Battery类中也许是合适的;
    # 但如果要描述一家汽车制造商的整个产品线，也许应该将方法get_range()移到ElectricCar 类中。
# 在这种情况下，get_range()依然根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。
# 我们也可以这样做:
    # 将方法get_range()还留在Battery类中，但向它传递一个参数，如 car_model;
    # 在这种情况下，方法get_range()将根据电瓶容量和汽车型号报告续航里程。
# 这让你进入了程序员的另一个境界:
    # 解决上述问题时，你从较高的逻辑层面(而不是语法层面)考虑;
    # 你考虑的不是Python，而是如何使用代码来表示实物。
    # 到达这种境界后，你经常会发现，现实世界的建模方法并没有对错之分。
    # 有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。
    # 只要代码像你希望的那样运行，就说明你做得很好!
    # 即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁;
    # 要编写出高效、准确的代码，都得经过这样的过程。

