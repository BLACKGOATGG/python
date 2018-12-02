#======================================================
# 编程时经常需要检查一系列条件，并据此决定采取什么措施。
# if语句能够检查程序的当前状态，并据此采取相应的措施。
players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
eee = ""
for i in players:
    if i == "eee" :
        eee = i.upper()
        print(i.upper())
    else :
        print(i.title())

#======================================================
# 每条if语句的核心都是一个值为True或False的表达式,这种表达式被称为条件测试。
print("\n")

# 检查是否相等
print(1=="1",1==1)
print(eee=="eee",eee.lower()=="eee")

# 检查是否不等
print(1!="1",1!=1)
print(eee!="eee",eee.lower()!="eee")

# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于
print(1>1,1>=1)
print(1<1,1<=1)
