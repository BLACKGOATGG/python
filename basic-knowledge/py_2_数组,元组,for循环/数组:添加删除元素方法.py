#======================================================
motors = ['honda', 'yamaha', 'suzuki'] 
print(motors)

motors[0] = 'ducati'
print(motors)

#列表尾部添加元素
motors.append("ducati")
print(motors)

#在列表中插入元素:第一个参数为下标，第二个参数为插入的元素
motors.insert(0,"ducati")
print(motors)

#删除元素
#del 使用del可删除任何位置处的列表元素，条件是知道其索引
del motors[1]
print(motors)

#pop 删除指定位置的元素(默认是最后一位),返回值为被删除的元素
pop_motors_1 = motors.pop(0)
print(motors)
print(pop_motors_1)

#remove 根据值删除元素，只会删除第一个指定的元素
motors.remove("ducati")
print(motors)


#常用方法
motuos = []
motuos.append('honda') 
motuos.append('yamaha') 
motuos.append('suzuki')
print(motuos)


