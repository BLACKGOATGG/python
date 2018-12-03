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
print("\nif语句的核心")
# 每条if语句的核心都是一个值为True或False的表达式,这种表达式被称为条件测试。

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
print("\n同时检查多个条件")
# 有时候你需要在两个条件都为True时才执行相应的操作
# 而有时候你只要求一个条件为True时就执行相应的操作
# 为改善可读性，可将每个测试都分别放在一对括号内，但并非必须这样做

# 使用and检查多个条件,所有条件都为真最终结果为真，反之为假
print((1!="1") and (1==1))  #两个条件都为真
print((1!="1") and (1!=1))  #一个条件为真
print((1=="1") and (1!=1))  #两个条件为假

# 使用or检查多个条件，只要有一个条件为真最终结果就为真，反之为假
print((1!="1") or (1==1))  #两个条件都为真
print((1!="1") or (1!=1))  #一个条件为真
print((1=="1") or (1!=1))  #两个条件为假

#======================================================
print("\n检查特定值是否包含在列表中")
# 有时候，执行操作前必须检查列表是否包含特定的值。
# 结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
# 在地图程序中，可能需要检查用户提交的 位置是否包含在已知位置列表中。
# 要判断特定的值是否已包含在列表中，可使用关键字in。

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
print("\n布尔表达式")
# 术语：布尔表达式，是条件测试的别名。
# 与条件表达式一样，布尔表达式的结果要么为True，要么为False。
# 布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容

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
print("\nif,elif else")
# 经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构。
# Python只执行 if-elif-else结构中的一个代码块
# 它依次检查每个条件测试，直到遇到通过了的条件测试。
age = 12
price=0
if age < 4:
    price=0
elif age < 18:
    price=5
elif age < 65:
    price=10
else:
    price = 5
print("你的入场费用是 $" + str(price) + ".")

# Python并不要求if-elif结构后面必须有else代码块。
# 在有些情况下，else代码块很有用;
# 而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰
if age < 4:
    price=0
elif age < 18:
    price=5
elif age < 65:
    price=10
elif age >= 65: 
    price = 5
print("你的入场费用是 $" + str(price) + ".")

# if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况:
# 遇到通过了的测试后，Python就跳过余下的测试。
# 这种行为很好，效率很高，让你能够测试一个特定的条件。
# 然而，有时候必须检查你关心的所有条件。
# 在这种情况下，应使用一系列不包含elif和else 代码块的简单if语句。
# 在可能有多个条件为True，
# 且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。
print("\n")
requested_toppings = ['蘑菇', '奶酪']
if '蘑菇' in requested_toppings:
    print("加 蘑菇.")
if '香肠' in requested_toppings:
    print("加 香肠.")
if '奶酪' in requested_toppings:
    print("加 奶酪.")
print("你的披萨做好了!")

# 如果只想执行一个代码块，就使用if-elif-else结构;
# 如果要运行多个代码块，就使用一系列独立的if语句。

#======================================================
print("\n使用if语句处理列表")














