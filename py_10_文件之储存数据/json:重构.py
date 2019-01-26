# ===========================================================
print('\n重构')
# 你经常会遇到这样的情况:
    # 代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。
    # 这样的过程被称为重构。
    # 重构让代码更清晰、更易于理解、更容 易扩展。
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    username = ''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
                username = json.load(f_obj)

    except FileNotFoundError:
        return None
    
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input('what is your name?')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)

    return username


def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")

    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()