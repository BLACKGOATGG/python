#======================================================
# 列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，这对处理网 站的用户列表或游戏中的角色列表至关重要。
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
print(len(bicycles))
print("0",bicycles[0])
print(bicycles[0].title())
print("1",bicycles[1])
print("2",bicycles[2])
print("-1",bicycles[-1])
print("-2",bicycles[-2])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
