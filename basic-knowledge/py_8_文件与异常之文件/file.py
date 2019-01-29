# ===========================================================
print('文件与异常')
# 至此，你掌握了编写组织有序而易于使用的程序所需的基本技能，该考虑让程序目标更明确、用途更大了。
# 本章学习内容：
    # 在本章中，你将学习处理文件，让程序能够快速地分析大量的数据;
    # 你将学习错误处理，避免程序在面对意外情形时崩溃;
    # 你将学习异常，它们是Python创建的特殊对象，用于管理程序运行时出现的错误;
    # 你还将学习模块json，它让你能够保存用户数据，以免在程序停止运行后丢失。

# 学习处理文件和保存数据可让你的程序使用起来更容易:
    # 用户将能够选择输入什么样的数据，以及在什么时候输入;
    # 用户使用你的程序做一些工作后，可将程序关闭，以后再接着往下做。
    # 学习处理异常可帮助你应对文件不存在的情形，以及处理其他可能导致程序崩溃的问题。
    # 这让你的程序在面对错误的数据时更健壮——不管这些错误数据源自无意的错误，还是源自破坏程序的恶意企图。
# 你在本章学习的技能可提高程序的适用性、可用性和稳定性。

# ===========================================================
print('\n从文件中读取数据')
# 文本文件可存储的数据量多得难以置信:天气数据、交通数据、社会经济数据、文学作品等。
# 每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。
    # 例如，你可以编写一个这样的程序:
    # 读取一个文本文件的内容，重新设置这些数据的格式并将其写入文件，让浏览器能够显示这些内容。

# 要使用文本文件中的信息，首先需要将信息读取到内存中。
# 为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。

# ===========================================================
print('\n读取整个文件')
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。

# 函数open()接受一个参数: 要打开的文件的名称。
# Python在当前执行的文件所在的目录中查找指定的文件。
# 在这个示例中，当前运行的是file.py，因此Python在file.py所在的目录中查找pi_digits.txt。

# 函数open() 返回一个表示文件的对象。
# 在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象;
# Python将这个对象存储在我们将在后面使用的变量中。

# 关键字with在不再需要访问文件后将其关闭。
# 在这个程序中，注意到我们调用了open()，但没有调用close();
# 你也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。
# 这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。
# 如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭(无法访问)，这会导致更多的错误。
# 并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定:
# 你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

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

# 東南に行き 僕は君に恋し 三百六十五日 忘れることない Je　Le sais continue c’ est pas bon，（我已知道如若继续下去）A la fin tu restes pas longtemps （总有一天彼此会分离） 僕はいつも　Waiting For You


# ===========================================================
print('\n使用文件的内容')
# 将文件读取到内存中后，就可以以任何方式使用这些数据了。

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)    

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 注意
# 读取文本文件时，Python将其中的所有文本都解读为字符串。
# 如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数。


# ===========================================================
print('\n包含一百万位的大型文件')
# 对于你可处理的数据量，Python没有任何限制;
# 只要系统的内存足够多，你想处理多少数据都可以。

filename = 'pi_digits_big.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))


# ===========================================================
print('\n圆周率值中包含你的生日吗')
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。
# 如果不包含索引值，返回-1。
# 可使用方法 replace()将字符串中的特定单词都替换为另一 个单词。

filename = 'pi_digits_big.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

# birthday = input("Enter your birthday, in the form mmddyy: ")
birthday = '990617'
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print('location: ', pi_string.find(birthday)+1 )
else:
    print("Your birthday does not appear in the first million digits of pi.")






