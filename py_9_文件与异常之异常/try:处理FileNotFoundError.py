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