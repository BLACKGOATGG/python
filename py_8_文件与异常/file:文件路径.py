# ===========================================================
print('\n文件路径')
# 当你将类似pi_digits.txt这样的简单文件名传递给函数open()时，Python将在当前执行的文件(即.py程序文件)所在的目录中查找文件。
# 根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。

# with open('./call.html') as file_object:
# with open('./../test/d.txt') as file_object:
with open('./text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 在Linux和OS X中，你可以这样编写代码:
    # with open('text_files/filename.txt') as file_object:

# 在 Windows系统中，在文件路径中使用反斜杠(\)而不是斜杠(/):
    # with open('text_files\filename.txt') as file_object:

# 相对文件路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。这称为相对文件路径。
# 相对文件路径来打开该文件夹中的文件。
# 你还可以将文件在计算机中的准确位置告诉Python，这样就不用关心当前运行的程序存储在什么地方了。这称为绝对文件路径。
# 通过使用绝对路径，可读取系统任何地方的文件。

# 绝对路径通常比相对路径更长，因此将其存储在一个变量中，再将该变量传递给open()会有所帮助。
# 在Linux和OS X中，绝对路径类似于下面这样:
    # file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
    # with open(file_path) as file_object:
# 而在Windows系统中，它们类似于下面这样:
    # file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
    # with open(file_path) as file_object:

# 注：Windows系统有时能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且结果不符合预期，请确保在文件路径中使用的是反斜杠