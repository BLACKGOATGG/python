#======================================================
print("\n使用if语句处理列表")
# 通过结合使用if语句和列表，可完成一些有趣的任务:
# 对列表中特定的值做特殊处理;
# 高效地管理不断变化的情形，如餐馆是否还有特定的食材;
# 证明代码在各种情形下都将按预期那样运行。
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': 
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

# 到目前为止，对于处理的每个列表都做了一个简单的假设，
# 即假设它们都至少包含一个元素。 
# 我们马上就要让用户来提供存储在列表中的信息，
# 因此不能再假设循环运行时列表不是空的。
# 有鉴于此，在运行for循环前确定列表是否为空很重要。
print("\n")
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []
if requested_toppings: 
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers': 
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")        
else:
    print("Are you sure you want a plain pizza?")

# 使用多个列表
print("\n")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
if requested_toppings: 
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")