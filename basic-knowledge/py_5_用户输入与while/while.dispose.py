# ===========================================================
print('使用while循环来处理列表和字典')
# for循环是一种遍历列表的有效方式
# 但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while循环。
# 通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入
# 供以后查看和显示。


print('\n在列表之间移动元素')
# 列表为空的时候检测为False
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed:") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print('\n删除包含特定值的所有列表元素')
#remov() 根据值删除元素，只会删除第一个指定的元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: 
    pets.remove('cat')
print(pets)


print('\n使用用户输入来填充字典')
responses = {}

while True:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将答卷存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (y/ n) ")
    if repeat == 'n': 
        break

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

