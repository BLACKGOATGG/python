#======================================================
print("\nif语句")
# 编程时经常需要检查一系列条件，并据此决定采取什么措施。
# if语句能够检查程序的当前状态，并据此采取相应的措施。
players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
eee = ""
for i in players:
    if i == "eee" :
        eee = i.upper()
        print(i.upper())
    else :
        print(i.title())

#======================================================
# 每条if语句的核心都是一个值为True或False的表达式,这种表达式被称为条件测试。
print("\nif语句的核心")

# 检查是否相等
print(1=="1",1==1)
print(eee=="eee",eee.lower()=="eee")

# 检查是否不等
print(1!="1",1!=1)
print(eee!="eee",eee.lower()!="eee")

# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于
print(1>1,1>=1)
print(1<1,1<=1)

#======================================================
# 同时检查多个条件
# 有时候你需要在两个条件都为True时才执行相应的操作
# 而有时候你只要求一个条件为True时就执行相应的操作
# 为改善可读性，可将每个测试都分别放在一对括号内，但并非必须这样做
print("\n同时检查多个条件")

# 使用and检查多个条件,所有条件都为真最终结果为真，反之为假
print((1!="1") and (1==1))  #两个条件都为真
print((1!="1") and (1!=1))  #一个条件为真
print((1=="1") and (1!=1))  #两个条件为假

# 使用or检查多个条件，只要有一个条件为真最终结果就为真，反之为假
print((1!="1") or (1==1))  #两个条件都为真
print((1!="1") or (1!=1))  #一个条件为真
print((1=="1") or (1!=1))  #两个条件为假

#======================================================
# 检查特定值是否包含在列表中
# 有时候，执行操作前必须检查列表是否包含特定的值。
# 结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
# 在地图程序中，可能需要检查用户提交的 位置是否包含在已知位置列表中。
# 要判断特定的值是否已包含在列表中，可使用关键字in。
print("\n检查特定值是否包含在列表中")

news = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new = "fff"
# 检查特定值是否包含在列表中
if new in news:
    print(news)
else:
    print(news)

# 检查特定值是否不包含在列表中
if new not in news:
    news.append(new)
    print(news)
else:
    print(news)

#======================================================
# 布尔表达式
# 术语：布尔表达式，是条件测试的别名。
# 与条件表达式一样，布尔表达式的结果要么为True，要么为False。
# 布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容
print("\n布尔表达式")

news = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new = "fff"
boolean_one = 1==1
boolean_two = False
boolean_three = new in news

# if boolean_one:
#     print("boolean_one "+str(boolean_one))
# else :
#     print("boolean_one "+str(boolean_one))

# if boolean_two:
#     print("boolean_two "+str(boolean_two))
# else :
#     print("boolean_two "+str(boolean_two))

# if boolean_three:
#     print("boolean_three "+str(boolean_three))
# else :
#     print("boolean_three "+str(boolean_three))
if boolean_one:
    print("boolean_one",boolean_one)
else :
    print("boolean_one",boolean_one)

if boolean_two:
    print("boolean_two",boolean_two)
else :
    print("boolean_two",boolean_two)

if boolean_three:
    print("boolean_three",boolean_three)
else :
    print("boolean_three",boolean_three)

# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。

#======================================================
# if,elif else
# 经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构。
# Python只执行 if-elif-else结构中的一个代码块
# 它依次检查每个条件测试，直到遇到通过了的条件测试。
print("\nif,elif else")

age = 12
price=0
if age < 4:
    price=0
elif age < 18:
    price=5
else:
    price=10

print("你的入场费用是 $" + str(price) + ".")


















