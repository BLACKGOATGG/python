# ===========================================================
print('\n异常')
# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时，它都会创建一个异常对象。
    # 如果你编写了处理该异常的代码，程序将继续运行;
    # 如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。

# 异常是使用try-except代码块处理的。
# try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
# 使用了try-except代码块时，即便出现异常，程序也将继续运行: 
    # 显示你编写的友好的错误消息，而不是令用户迷惑的traceback。


# ===========================================================
print('\n处理ZeroDivisionError异常')
# 下面来看一种导致Python引发异常的简单错误。你可能知道不能将一个数字除以0，但我们还是让Python这样做吧

# print(5/0)

# 显然，Python无法这样做，因此你将看到一个traceback:
# 在上述traceback中，Ø处指出的错误ZeroDivisionError是一个异常对象。
# Python无法按你的要求做时，就会创建这种对象。
# 在这种情况下，Python将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。
# 下面我们将告诉Python，发生这种错误时怎么办;
# 这样，如果再次发生这样的错误，我们就有备无患了。


# ===========================================================
print('\n使用try-except代码块')
# 当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
# 你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。

# 处理ZeroDivisionError异常的try-except代码块类似于下面这样:
try:
    print(5/0)
    # print(5/1)
except ZeroDivisionError:
    print("try-except: You can't divide by zero!")

# 我们将导致错误的代码行print(5/0)放在了一个try代码块中。
    # 如果try代码块中的代码运行起来没有问题，Python将跳过except代码块;
    # 如果try代码块中的代码导致了错误，Python将查找 这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
# 在这个示例中，try代码块中的代码引发了ZeroDivisionError异常，因此Python指出了该如何解决问题的except代码块，并运行其中的代码。
# 这样，用户看到的是一条友好的错误消息，而不是traceback:
    # You can't divide by zero! 
# 如果try-except代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处理这种错误。
# 下面来看一个捕获错误后程序将继续运行的示例。


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

print("输入两个数字，获得他们的商")
print("输入q退出")
while True:
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








