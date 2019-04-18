# ===========================================================
print('\n传递列表')
# 经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象(如字典)。
# 将列表传递给函数后，函数就能直接访问其内容。
def greet_users(names): 
    """向列表中的每位用户都发出简单的问候""" 
    for name in names:
        msg = "Hello, " + name.title() + "!" 
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


print('\n在函数中修改列表')
# 将列表传递给函数后，函数就可对其进行修改。
# 在函数中对这个列表所做的任何修改都是永久性的，这能够高效地处理大量的数据。
def print_models(unprinted_designs, completed_models): 
    """模拟打印每个设计，直到没有未打印的设计为止打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models): 
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print(unprinted_designs)


print('\n禁止函数修改列表')
# 有时候，需要禁止函数修改列表。
# 为解决这个问题，可向函数传递列表的副本而不是原件;
# 这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
# 切片表示法[:]创建列表的副本。

unprinted_designs_two = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models_two = []

print_models(unprinted_designs_two[:],completed_models_two)
show_completed_models(completed_models_two)

print(unprinted_designs_two)

