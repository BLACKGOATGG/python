# ===========================================================
print('\n使用类和实例')
# 可以使用类来模拟现实世界中的很多情景。
# 类编写好后，你的大部分时间都将花在使用根据类创建的实例上。
# 你需要执行的一个重要任务是修改实例的属性。
# 你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。

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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


print('\n给属性指定默认值')
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。
# 在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的;
# 如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

my_new_car.read_odometer()


print('\n修改属性的值')
# 可以以三种不同的方式修改属性的值:
    # 直接通过实例进行修改;
    # 通过方法进行设置;
    # 通过方法进行递增(增加特定的值)。

print('\n1. 直接修改属性的值')
# 1. 直接修改属性的值
# 要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为23:
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法。

print('\n2. 通过方法修改属性的值')
# 2. 通过方法修改属性的值
# 如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print('\n3. 通过方法对属性的值进行递增')
# 3. 通过方法对属性的值进行递增
# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
my_new_car.increment_odometer(1)
my_new_car.read_odometer()
my_new_car.increment_odometer(3)
my_new_car.read_odometer()
my_new_car.increment_odometer(-1)
my_new_car.read_odometer()

