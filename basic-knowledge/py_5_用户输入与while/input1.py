# ===========================================================
print('用户输入和while循环')
# 大多数程序都旨在解决最终用户的问题，为此通常需要从用户那 里获取一些信息。
# 过获取用户输入并学会控制程序的运行时间，可编写出交互式程序。
# 学习如何让程序不断地运行，让用户能够根据需要输入信息，并在程序中使用这些信息。
# 为此，需要使用while循环让程序不断地运行，直到指定的条件不满足为止。

# ===========================================================
print('\n函数input()的工作原理')
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，
# Python将其存储在 一个变量中，以方便使用。
# 函数input()接受一个参数:即要向用户显示的提示或说明，让用户知道该如何做。

message = input("Tell me something, and I will repeat it back to you: ") 
print(message)


print('\n编写清晰的程序')
# 有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。
# 在这种情况下， 可将提示存储在一个变量中，再将该变量传递给函数input()。
# 这样，即便提示超过一行，input() 语句也非常清晰。

prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")


print('\n使用int()来获取数值输入')
# 使用函数input()时，Python将用户输入解读为字符串。
# 试图将输入用于数值比较时，Python会引发错误
# 因为它无法将字符串和整数进行比较
# 为解决这个问题，可使用函数int()，它让Python将输入视为数值。
# 函数int()将数字的字符 串表示转换为数值表示，

age = input("How old are you? ")
print(age[0])
age = int(age)
print(age)
# print(age[0])
if age >= 36:
    print("You're tall enough to ride!")
else:
    print("error")




