#======================================================
print("\n字典")
# 字典是一系列键—值对。
# 每个键都与一个值相关联，可以使用键来访问与之相关联的值。
# 与键相关联的值可以是数字、字符串、列表乃至字典。
# 事实上，可将任何Python对象用作字典中的值。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])
print(alien_0["points"])
print(alien_0)

# 添加键—值对
print("\n添加键—值对")
# 字典是一种动态结构，可随时在其中添加键—值对。
# 要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)

# 先创建一个空字典
print("\n创建一个空字典")
# 有时候，在空字典中添加键—值对是为了方便，而有时候必须这样做。
# 为此，可先使用一对空的花括号定义一个字典，再分行添加各个键—值对。
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# 使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，
# 通常都需要先定义一个空字典。

# 修改字典中的值
print("\n修改字典中的值")
# 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print("\n修改字典中的值2")
# 对一个能够以不同速度移动的外星人的位置进行跟踪。
# 为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    # 这个外星人的速度一定很快 
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键—值对
print("\n删除键—值对")
# 对于字典中不再需要的信息，可使用del语句将相应的键—值对彻底删除。
# 使用del语句时，必须指定字典名和要删除的键。方法与列表相同
# 删除的键—值对永远消失了。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
