# ===========================================================
print('\n保存用户生成的数据')
# 对于用户生成的数据，使用json保存它们大有裨益
# 因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
import json

# username = input('what is your name?')

""" filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, " + username + "!")
 """


# ===========================================================
# 使用json.load()将存储在username.json中的信息读取到变量username中。
# 恢复用户名后，我们就可以欢迎用户回来了:
import json

""" print('\n读取用户生成的数据')
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
 """


# ===========================================================
print('\n保存与读取用户生成的数据')
# 我们需要将这两个程序合并到一个程序中。
# 这个程序运行时，我们将尝试从文件username.json中获取用户名，因此我们首先编写一个尝试恢复用户名的try代码块。
# 如果这个文件不存在，我们就在except代码块中提示用户输入用户名，并将其存储在username.json中，以便程序再次运行时能够获取它:
import json

username = ''
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = input('what is your name?')
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username + "!")

else:
    print("Welcome back, " + username + "!")

