# ===========================================================
print('\n求模运算符')
# 处理数值信息时，求模运算符(%)是一个很有用的工具
# 它将两个数相除并返回余数
# 求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
# 如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。
# 可利用这一点,来判断一个数是奇数还是偶数:

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
# 偶数都能被2整除，因此对一个数(number)和2执行求模运算的结果为零
# 即number % 2 == 0
# 那么这个数就是偶数;
# 否则就是奇数。






