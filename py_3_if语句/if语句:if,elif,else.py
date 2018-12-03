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
