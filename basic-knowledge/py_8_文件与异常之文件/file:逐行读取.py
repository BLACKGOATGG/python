# ===========================================================
print('\n逐行读取')
# 读取文件时，常常需要检查其中的每一行:
# 你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    
# 我们将要读取的文件的名称存储在变量filename中，这是使用文件时一种常见的做法。
# 由于变量filename表示的并非实际文件——它只是一个让Python知道到哪里去查找文件的字符串
# 因此可轻松地将'pi_digits.txt'替换为你要使用的另一个文件的名称。

# 这里也使用了关键字with，让Python负责妥善地打开和关闭文件。
# 为查看文件的内容，我们通过对文件对象执行循环来遍历文件中的每一行。