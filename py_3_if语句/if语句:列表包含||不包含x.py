#======================================================
print("\n检查特定值是否包含在列表中")
# 有时候，执行操作前必须检查列表是否包含特定的值。
# 结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
# 在地图程序中，可能需要检查用户提交的 位置是否包含在已知位置列表中。
# 要判断特定的值是否已包含在列表中，可使用关键字in。

news = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new = "fff"
# 检查特定值是否包含在列表中
if new in news:
    print(news)
else:
    print(news)

# 检查特定值是否不包含在列表中
if new not in news:
    news.append(new)
    print(news)
else:
    print(news)
