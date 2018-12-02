cars = ['bmw', 'audi', 'toyota', 'subaru']

#obj.sort()方法---永久性排序
#默认 按字母顺序排序
cars.sort()
print(cars)

#传递参数reverse=True：字母顺序的相反排序!此处t要大写
cars.sort(reverse=True)
print(cars)


#sorted(obj)方法---非永久性排序：返回排序后的数组，原数组保持不变
#默认 按字母顺序排序
print(sorted(cars))
print(cars)

#传递参数reverse=True：字母顺序的相反排序!此处t要大写
cars.sort()
print(cars)
print(sorted(cars,reverse=True))
print(cars)


#obj.reverse()方法用来反转列表，效果是永久性的，想恢复到原来的列表再次使用reverse就行
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#len(obj)方法返回列表的长度
print(len(cars))


