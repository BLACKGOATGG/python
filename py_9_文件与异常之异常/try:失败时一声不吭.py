# ===========================================================
print('\n失败时一声不吭')
# 在前一个示例中，我们告诉用户有一个文件找不到。
# 但并非每次捕获到异常时都需要告诉用户，有时候你希望程序在发生异常时一声不吭，就像什么都没有发生一样继续运行。
# 要让程序在失败时一声不吭，可像通常那样编写try代码块，但在except代码块中明确地告诉Python什么都不要做。
# Python有一个pass语句，可在代码块中使用它来让Python什么都不要做:

def count_words_2(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("文件 " + filename + " 大概包含 " + str(num_words) + " 个单词.")

filenames = ['python.txt', 'alice.txt', 'try.py']
for filename in filenames:
    count_words_2(filename)

# 相比于前一个程序，这个程序唯一不同的地方是Ø处的pass语句。
# 现在，出现 FileNotFoundError异常时，将执行except代码块中的代码，但什么都不会发生。
# 这种错误发生时，不会出现traceback，也没有任何输出。
# 用户将看到存在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到:
# 文件 python.txt 大概包含 6042 个单词.
# 文件 try.py 大概包含 461 个单词.

# pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。
# 例如，在这个程序中，我们可能决定将找不到的文件的名称写入到文件 missing_files.txt中。
# 用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到的问题。



