# ===========================================================
print('\n在一个模块中存储多个类')
# 虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。

print('\n在一个模块中导入另一个模块')
# 有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
# 将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。
# 在这种情况下，可在前一个模块中导入必要的类。
# ！！！！！！！！！！！！！！！！！（此处未实践）！！！！！！！！！！！！！！！！！！！！！！！


"""一个可用于表示汽车的类""" 
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage): 
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70): 
        """初始化电瓶的属性""" 
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self): 
        """打印一条描述电瓶续航里程的消息""" 
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()







