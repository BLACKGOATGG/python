#======================================================
# 布尔表达式
# 术语：布尔表达式，是条件测试的别名。
# 与条件表达式一样，布尔表达式的结果要么为True，要么为False。
# 布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容
print("\n")

news = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new = "fff"
boolean_one = 1==1
boolean_two = False
boolean_three = new in news

if boolean_one:
    print("boolean_one True")
else :
    print("boolean_one false")

if boolean_two:
    print("boolean_two True")
else :
    print("boolean_two false")

if boolean_three:
    print("boolean_three True")
else :
    print("boolean_three false")

# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。