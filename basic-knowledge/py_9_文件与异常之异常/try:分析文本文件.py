# ===========================================================
print('\n分析文本文件')
# 你可以分析包含整本书的文本文件。
# 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
# 结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。
# 方法 count()来确定特定的单词或短语在字符串中出现了多少次。

filename = 'python.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "文件" + filename + " 不存在"
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("文件 " + filename + " 大概包含 " + str(num_words) + " 个单词.")
