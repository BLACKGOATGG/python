#======================================================
print("\n遍历字典")
# 一个Python字典可能只包含几个键—值对，也可能包含数百万个键—值对。
# 鉴于字典可能包含大量的数据，Python支持对字典遍历。
# 字典可用于以各种方式存储信息，因此有多种遍历字典的方式:
# 可遍历字典的所有键—值对、键或值。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 遍历所有的键—值对
print("\n遍历所有的键—值对")
# 要编写用于遍历字典的for循环，方法items()很有用。
# 可声明两个变量，用于存储键—值对中的键和值。 
# 对于这两个变量，可使用任何名称
for name, language in favorite_languages.items():
    print("key:" + name.title() + "\nval:" + language.title())

# 遍历字典中的所有键
print("\n遍历字典中的所有键")
# 在不需要使用字典中的值时，方法keys()很有用。
# 可声明一个变量，用于存储键—值对中的键。 
# 对于这一个变量，可使用任何名称
for name in favorite_languages.keys():
    print("key:" + name.title())

# 遍历字典中的所有键2
print("\n遍历字典中的所有键2")
# 遍历字典时，会默认遍历所有的键
# 因此，如果将上述代码中的
# for name in favorite_ languages.keys():
# 替换为for name in favorite_languages:，
# 输出将不变。
friends = ['phil', 'sarah' , 'aa']
for name in friends:
    print(name.title())
    # 方法keys()并非只能用于遍历;
    # 实际上，它返回一个列表，其中包含字典中的所有键，
    if name in favorite_languages.keys():
        print(" Hi " + name.title() +
            ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")
    else:
        print("hi, please take our poll!")

# 按顺序遍历字典中的所有键
print("\n按顺序遍历字典中的所有键")
# 字典总是明确地记录键和值之间的关联关系
# 但获取字典的元素时，获取顺序是不可预测的。
# 这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
# 要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。
# 为此，可使用函数sorted()来获得按特定顺序排列的键列表的副本:
print(favorite_languages.keys())
print(sorted(favorite_languages.keys()))
print(sorted(set(favorite_languages.keys())))

# 遍历字典中的所有值
print("\n遍历字典中的所有值")
# 如果只要字典包含的值，可使用方法values()。
# 它返回一个值列表，而不包含任何键
# 可声明一个变量，用于存储键—值对中的值。 
# 对于这一个变量，可使用任何名称
for value in favorite_languages.values():
    print("values:" + value.title())

# 遍历字典中的所有值2
print("\n遍历字典中的所有值2")
# 这种做法提取字典中所有的值，而没有考虑是否重复。
# 涉及的值很少时，这也许不是问题，
# 但如果被调查者很多，最终的列表可能包含大量的重复项。
# 为剔除重复项，可使用集合(set)。 
# 集合类似于列表，但每个元素都必须是独一无二的:
print(favorite_languages.values())
print(sorted(favorite_languages.values()))
print(sorted(set(favorite_languages.values())))
for value in set(favorite_languages.values()):
    print("values:" + value.title())

# 通过对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素，
# 并使用这些元素来创建一个集合。