# ===========================================================
print('\n使用break退出循环')
# 在任何Python循环中都可使用break语句。
# 例如，可使用break语句来退出遍历列表或字典的for循环。
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
active = True 
message = "" 

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print(active)
        # 要立即退出while循环，不再运行循环中余下的代码
        # 也不管条件测试的结果如何，可使用 break语句。
        # break语句用于控制程序流程，可使用它来控制哪些代码行将执行
        # 哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
        break
        print(active)
    else:  
        print(message)

            