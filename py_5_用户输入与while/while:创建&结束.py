# ===========================================================
print('while 循环')
# for循环用于针对集合中的每个元素都一个代码块
# 而while循环不断地运行，直到指定的条件不满足为止。

print('\n使用while循环')

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print('\n避免无限循环')
# 每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
# 如上面代码不小心遗漏了代码行current_number += 1，将形成死循环
# 要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。
# 如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值;
# 如果在这种情况下程序没有结束，请检查程序处理这个值的方式
# 确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。



print('\n让用户选择何时退出')
# 可使用while循环让程序在用户愿意时不断地运行
# 我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
active = True 
message = "" 

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:  
        print(message)


