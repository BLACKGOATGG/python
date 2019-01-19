# ===========================================================
print('\n创建一个包含文件各行内容的列表')
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
# 如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表:
# 你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 在111处，方法readlines()从文件中读取每一行，并将其存储在一个列表中;
# 接下来，该列表被存储到变量lines中;
# 在with代码块外，我们依然可以使用这个变量。

# 在113处，我们使用一个简单的for循环来打印lines中的各行。
# 由于列表lines的每个元素都对应于文件中的一行，
# 因此输出与文件内容完全一致。