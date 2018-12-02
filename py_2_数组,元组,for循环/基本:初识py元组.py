#初识元组

# 列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，这对处理网 站的用户列表或游戏中的角色列表至关重要。
# 然而，有时候你需要创建一系列不可修改的元素， 元组可以满足这种需求。
# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。
dimensions = (200, 100 , 50)
print(dimensions)

# 定义元组后，就可以使用索引来 访问其元素，就像访问列表元素一样。
print(dimensions[0])
print(dimensions[1])
print(dimensions[-1])

# 修改第一个元素的值，导致Python返回类型错误消息。
# 由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值
# dimensions[1] = 60
print("\n")
for i in dimensions:
    print(i)

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
# 因此，如果要修改前述矩形的尺寸，可重新定义整个元组
dimensions = (200, 100 , 50 , 20 , "10")
print(dimensions)
