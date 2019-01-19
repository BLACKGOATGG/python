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