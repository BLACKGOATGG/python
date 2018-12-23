# ===========================================================
print('\n在循环中使用continue')
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环
# 可使用continue语句
# 它不像break语句那样不再执行余下的代码并退出整个循环。
# 意义：跳出本次循环，进行下次循环

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: 
        continue
    print(current_number)

            