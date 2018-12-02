#学到数组切片了
players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print("players",players)
#常用方法一：参数一表示开始的下标，参数二标示结束的下标
print("players[0:3]",players[0:3])
print("players[1:4]",players[1:4])

#如果没有指定开始索引python自动从下标0开始提取
print("players[:2]",players[:2])

#没有指定终止索引同上，从开始索引一直到列表末尾
print("players[2:]",players[2:])

#负数索引返回离列表末尾相应距离的元素
print("players[:-3]",players[:-3])
print("players[-3:]",players[-3:])

#配合for循环使用
for i in players[:3]:
	print(i.title())


#数组拷贝:listone方法为引用型赋值,listtow为真实赋值
listone = players
listtow = players[:]

print("\n")
print(players)
print(listone)
print(listtow)

#引用型赋值父类值发生改变会影响子类，真实赋值则父类子类完全独立
players.append("fff")

print("\n")
print(players)
print(listone)
print(listtow)

#引用型赋值子类值发生改变也会影响父类
listone.append("ggg")
listtow.append("真实赋值子类")

print("\n")
print(players)
print(listone)
print(listtow)
