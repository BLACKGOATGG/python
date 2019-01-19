# ===========================================================
print('类')
# 面向对象编程是最有效的软件编写方法之一。
# 在面向对象编程中， 你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
# 编写类时，你定义一大类对象都有的通用行为。
# 基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。
# 使用面向对象编程可模拟现实情景，其逼真程度达到了令你惊讶的地步。

print('\n创建和使用类')
# 使用类几乎可以模拟任何东西。
# 根据类来创建对象被称为实例化，这让你能够使用类的实例。

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name 
        self.age = age 
        print(self.name,self.age)
    
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + "rolled over!")

# 类中的函数称为方法;前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。

# 1. 方法__init__()
# 方法__init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。
# 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。

# 我们将方法__init__()定义成了包含三个形参:self、name和age。在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面。
# 为何必须在方法定义中包含形参self呢?因为 Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。

# 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。 
# 我们创建Dog实例时，Python将调用Dog类的方法__init__()。
# 我们将通过实参向Dog()传递名字和年龄; self会自动传递，因此我们不需要传递它。
# 每当我们根据Dog类创建实例时，都只需给最后两个形参(name和age)提供值。

# __init__处定义的两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，我们可以通过类的任何实例来访问这些变量。
# self.name = name获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例。
# self.age = age的作用与此类似。

# Dog类还定义了另外两个方法:sit()和roll_over()(见)。由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参self。


print('\n根据类创建实例')
# 可将类视为有关如何创建实例的说明。

my_dog = Dog('我狗', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# 在54处，我们让Python创建一条名字为'willie'、 年龄为6的小狗。
# 遇到这行代码时，Python使用实参'willie'和6调用Dog类中的方法__init__()。
# 方法__init__()创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name和age。
# 方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例。
# 我们将这个实例存储在变量my_dog中。
# 在这里，命名约定很有用:我们通常可以认为首字母大写的名称(如 Dog)指的是类，而小写的名称(如my_dog)指的是根据类创建的实例。

# 1. 访问属性
# 要访问实例的属性，可使用句点表示法。句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值。
# 在这里，Python 先找到实例my_dog，再查找与这个实例相关联的属性name。
# 在Dog类中引用这个属性时，使用的是self.name。
# 在57处，我们使用同样的方法来获取属性age的值。
# 在前面的第1条print语句中， my_dog.name.title()将my_dog的属性name的值'willie'改为首字母大写的;
# 在第2条print语句中， str(my_dog.age)将my_dog的属性age的值6转换为字符串。
# 2. 调用方法
# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。
# 要调用方法，可指定实例的名称(这里是my_dog)和要调用的方法，并用句点分隔它们。
# 遇到代码my_dog.sit()时，Python在类Dog中查找方法sit()并运行其代码。
# Python以同样的方式解读代码my_dog.roll_over()。

# 这种语法很有用。如果给属性和方法指定了合适的描述性名称，如name、age、sit()和 roll_over()，
# 即便是从未见过的代码块，我们也能够轻松地推断出它是做什么的。


print('\n创建多个实例')
# 可按需求根据类创建任意数量的实例。

your_dog = Dog('你狗', 3)
her_dog = Dog('他狗', 5)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()

print("\nHer dog's name is " + her_dog.name.title() + ".")
print("Her dog is " + str(her_dog.age) + " years old.")
her_dog.sit()
her_dog.roll_over()


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

    def fill_gas_tank(self):
        """汽车油箱"""
        print("汽车油箱!")


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


# ===========================================================
print('\n继承')
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;
# 原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
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

