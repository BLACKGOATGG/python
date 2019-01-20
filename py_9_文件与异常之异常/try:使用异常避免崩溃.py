# ===========================================================
print('\n使用异常避免崩溃')
# 发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。
# 这种情况经常会出现在要求用户提供输入的程序中;
# 如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

# print("输入两个数字，获得他们的商")
# print("输入q退出")
# while True:
#     first_number = input("第一个数字")
#     if first_number == 'q':
#         break
#     second_number = input("第二个数字")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)

#     print('结果是：' , answer )

# 这个程序没有采取任何处理错误的措施，因此让它执行除数为0的除法运算时，它将崩溃:
# 程序崩溃可不好，但让用户看到traceback也不是好主意。
# 不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。
    # 例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。
    # 有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。


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

