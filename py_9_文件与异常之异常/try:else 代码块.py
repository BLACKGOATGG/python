# ===========================================================
print('\nelse 代码块')
# 通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。
# 这个示例还包含一个else代码块;依赖于try代码块成功执行的代码都应放到else代码块中:

print("输入两个数字，获得他们的商")
print("输入q退出")
while False:
# while True:
    first_number = input("第一个数字")
    if first_number == 'q':
        break
    second_number = input("第二个数字")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('不能将一个数字除以0')
    else:
        print('结果是：' , answer )

# try-except-else代码块的工作原理大致如下:
    # Python尝试执行try代码块中的代码;只有可能引发异常的代码才需要放在try语句中。
    # 有时候，有一些仅在try代码块成功执行时才需要运行的代码;这些代码应放在else代码块中。
    # except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
# 通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。

