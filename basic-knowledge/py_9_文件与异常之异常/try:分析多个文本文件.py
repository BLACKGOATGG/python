# ===========================================================
print('\n分析多个文本文件')
# 这些代码大都与原来一样，我们只是将它们移到了函数count_words()中，并增加了缩进量。
# 修改程序的同时更新注释是个不错的习惯，因此我们将注释改成了文档字符串，并稍微调整了一下措辞(见Ø)。

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "文件 " + filename + " 不存在"
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("文件 " + filename + " 大概包含 " + str(num_words) + " 个单词.")

# filename = 'python.txt'
# count_words(filename)

# 现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。
# 为此，我们将要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用count_words()。

filenames = ['python.txt', 'alice.txt', 'try.py']
for filename in filenames:
    count_words(filename)


