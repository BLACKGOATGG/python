# ===========================================================
print('\n异常')
# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时，它都会创建一个异常对象。
    # 如果你编写了处理该异常的代码，程序将继续运行;
    # 如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。

# 异常是使用try-except代码块处理的。
# try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
# 使用了try-except代码块时，即便出现异常，程序也将继续运行: 
    # 显示你编写的友好的错误消息，而不是令用户迷惑的traceback。


# ===========================================================
print('\n处理ZeroDivisionError异常')
# 下面来看一种导致Python引发异常的简单错误。你可能知道不能将一个数字除以0，但我们还是让Python这样做吧

# print(5/0)

# 显然，Python无法这样做，因此你将看到一个traceback:
# 在上述traceback中，Ø处指出的错误ZeroDivisionError是一个异常对象。
# Python无法按你的要求做时，就会创建这种对象。
# 在这种情况下，Python将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。
# 下面我们将告诉Python，发生这种错误时怎么办;
# 这样，如果再次发生这样的错误，我们就有备无患了。


# ===========================================================
print('\n使用try-except代码块')
# 当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
# 你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。

# 处理ZeroDivisionError异常的try-except代码块类似于下面这样:
try:
    print(5/0)
    # print(5/1)
except ZeroDivisionError:
    print("try-except: You can't divide by zero!")

# 我们将导致错误的代码行print(5/0)放在了一个try代码块中。
    # 如果try代码块中的代码运行起来没有问题，Python将跳过except代码块;
    # 如果try代码块中的代码导致了错误，Python将查找 这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
# 在这个示例中，try代码块中的代码引发了ZeroDivisionError异常，因此Python指出了该如何解决问题的except代码块，并运行其中的代码。
# 这样，用户看到的是一条友好的错误消息，而不是traceback:
    # You can't divide by zero! 
# 如果try-except代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处理这种错误。
# 下面来看一个捕获错误后程序将继续运行的示例。


# ===========================================================
print('\n使用异常避免崩溃')
# 发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。
# 这种情况经常会出现在要求用户提供输入的程序中;
# 如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

print("输入两个数字，获得他们的商")
print("输入q退出")
while False:
# while True:
    first_number = input("第一个数字")
    if first_number == 'q':
        break
    second_number = input("第二个数字")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)

    print('结果是：' , answer )

# 这个程序没有采取任何处理错误的措施，因此让它执行除数为0的除法运算时，它将崩溃:
# 程序崩溃可不好，但让用户看到traceback也不是好主意。
# 不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。
    # 例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。
    # 有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。


# ===========================================================
print('\nelse 代码块')
# 通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。
# 这个示例还包含一个else代码块;依赖于try代码块成功执行的代码都应放到else代码块中:

print("输入两个数字，获得他们的商")
print("输入q退出")
while False:
# while True:
    first_number = input("第一个数字")
    if first_number == 'q':
        break
    second_number = input("第二个数字")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('不能将一个数字除以0')
    else:
        print('结果是：' , answer )

# try-except-else代码块的工作原理大致如下:
    # Python尝试执行try代码块中的代码;只有可能引发异常的代码才需要放在try语句中。
    # 有时候，有一些仅在try代码块成功执行时才需要运行的代码;这些代码应放在else代码块中。
    # except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
# 通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。


# ===========================================================
print('\n处理FileNotFoundError异常')
# 使用文件时，一种常见的问题是找不到文件:
    # 你要查找的文件可能在其他地方
    # 文件名可能不正确
    # 或者这个文件根本就不存在。
# 对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。

# filename = 'alice.txt'
# with open(filename) as f_obj:
#     contents = f_obj.read()

# Python无法读取不存在的文件，因此它引发一个异常:
    # Traceback (most recent call last):
    # File "try.py", line 116, in <module>
    #     with open(filename) as f_obj:
    # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# 在上述traceback中，最后一行报告了FileNotFoundError异常，这是Python找不到要打开的文件时创建的异常。
# 在这个示例中，这个错误是函数open()导致的，因此要处理这个错误，必须将try语句放在包含open()的代码行之前:

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "文件" + filename + " 不存在"
    print(msg)

# 在这个示例中，try代码块引发FileNotFoundError异常，因此Python找出与该错误匹配的 except代码块，并运行其中的代码。
# 最终的结果是显示一条友好的错误消息，而不是traceback:

# 如果文件不存在，这个程序什么都不做，因此错误处理代码的意义不大。
# 下面来扩展这个示例，看看在你使用多个文件时，异常处理可提供什么样的帮助。


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


# ===========================================================
print('\n决定报告哪些错误')
# 在什么情况下该向用户报告错误?在什么情况下又应该在失败时一声不吭呢?
    # 如果用户知道要分析哪些文件，他们可能希望在有文件没有分析时出现一条消息，将其中的原因告诉他们。
    # 如果用户只想看到结果，而并不知道要分析哪些文件，可能就无需在有些文件不存在时告知他们。
    # 向用户显示他不想看到的信息可能会降低程序的可用性。
    # Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。

# 编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误
# 但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。
# 凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。





