magicians = ['alice', 'david', 'carolina']

#py的普通常用for循环,基本与js的for-in一样
for i in magicians:
	print(i.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + i.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#range()方法能够生成一系列的数字
print(list(range(1,10)))
for j in range(1,5):
	print(j)

#range()方法可以指定步长
even_numbers = list(range(0,10,2))
print(even_numbers)

# 两个星号（**）代表乘方运算
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#min(),max(),sum()专门用于处理数字列表的Python函数，对应最小，最大，总和
print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))



