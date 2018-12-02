#======================================================
# if,elif else
# 经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构。
# Python只执行 if-elif-else结构中的一个代码块
# 它依次检查每个条件测试，直到遇到通过了的条件测试。
print("\n")

age = 12
price=0
if age < 4:
    price=0
elif age < 18:
    price=5
else:
    price=10

print("你的入场费用是 $" + str(price) + ".")