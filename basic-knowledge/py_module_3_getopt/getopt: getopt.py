"""
# 在运行程序时，可能需要根据不同的条件，输入不同的命令行选项来实现不同的功能。
# 目前有短选项和长选项两种格式。
    # 短选项格式为"-"加上单个字母选项；
    # 长选项为"--"加上一个单词。
# 长格式是在Linux下引入的。许多Linux程序都支持这两种格式。
# 在Python中提供了getopt模块很好的实现了对这两种用法的支持，而且使用简单。

# 取得命令行参数
# 在使用之前，首先要取得命令行参数。使用sys模块可以得到命令行参数。
"""
import sys

print(sys.argv)

"""
然后在命令行下敲入任意的参数，如：
-o t --help cmd file1 file2
可见，所有命令行参数以空格为分隔符，都保存在了sys.argv列表中。其中第1个为脚本的文件名。
"""


# 选项的写法要求
"""
对于短格式，"-"号后面要紧跟一个选项字母。如果还有此选项的附加参数，可以用空格分开，也可以不分开。
长度任意，可以用引号。如以下是正确的：
-o
-oa
-obbbb
-o bbbb
-o "a b"

对于长格式，"--"号后面要跟一个单词。如果还有些选项的附加参数，后面要紧跟"="，再加上参数。"="号前后不能有空格。如以下是正确的：

--help=file1

而这些是不正确的：
-- help=file1
--help =file1
--help = file1
--help= file1
"""


# 如何用getopt进行分析 
"""
使用getopt模块分析命令行参数大体上分为三个步骤：
    1.导入getopt, sys模块
    2.分析命令行参数
    3.处理结果

第一步很简单，只需要：
import getopt, sys
""" 
import sys
import getopt

"""
第二步处理方法如下（以Python手册上的例子为例）：
"""
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
#     print('分析出格式信息的命令行参数==>', opts)
#     print('不属于格式信息的命令行参数==>', args)
# except getopt.GetoptError:
#     print('help information and exit:')

def usage():
    """ usage()函数用于参数的说明帮助、当用户输入错误的参数时会输出相应的提示 """
    print('\n\nBHP Net Tool\n')
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen              - listen on [host]:[port] for incoming connections')
    print('-c --command             - execute the given file upon receiving a connection')
    print('-u --upload=destination  - initialize a command shell')
    print('-e --execute=file_to_run - upon receiving connection upload a file and write to [dextination]')
    print('\nExamples:')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\'cat /etc/passwd\'')
    print('echo: "ABCDEFGHI" | ./bhpnet.py -t 192.168.11.12 -p 135')
    sys.exit(0)

l = ['help', 'execute', 'listen', 'target', 'port', 'command', 'upload']
try:
    opts, args = getopt.getopt(sys.argv[1:], "he:lt:p:cu:", l)
    print('分析出格式信息的命令行参数==>', opts)
    print('不属于格式信息的命令行参数==>', args)
except getopt.GetoptError as err:
    print(str(err))
    usage()



print({'o':'开关及形参','a':'对应实参参数'})
for o,a in opts:
    print({'o':o,'a':a})
    if o in ('-h', '--help'):
        usage()
    elif o in ('-l', '--listen'):
        listen = True
    elif o in ('-e', '--execute'):
        execute = a
    elif o in ('-c', '--commandshell'):
        command = True
    elif o in ('-u', '--upload'):
        upload_destination = a
    elif o in ('-t', '--target'):
        target = a
    elif o in ('-p', '--port'):
        port = int(a)
    else:
        assert False,'Unhandled Option'



"""
1. 处理所使用的函数叫getopt()，因为是直接使用import导入的getopt模块，所以要加上限定getopt才可以。

2. 使用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）。

3. 使用短格式分析串"ho:"。当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。
当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。
所以"ho:"就表示"h"是一个开关选项；"o:"则表示后面应该带一个参数。

4. 使用长格式分析串列表：["help", "output="]。长格式串也可以有开关状态，即后面不跟"="号。
如果跟一个等号则表示后面还应有一个参数。这个长格式表示"help"是一个开关选项；"output="则表示后面应该带一个参数。

5. 调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。
opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。

6. 整个过程使用异常来包含，这样当分析出错时，就可以打印出使用信息来通知用户如何使用这个程序。


如上面解释的一个命令行例子为：
-h -o file --help --output=out file1 file2

在分析完成后，opts应该是：
[('-h', ''), ('-o', 'file'), ('--help', ''), ('--output', 'out')]

而args则为：
['file1', 'file2']
"""


"""
第三步主要是对分析出的参数进行判断是否存在，然后再进一步处理。主要的处理模式为：
for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    if o in ("-o", "--output"):
        output = a

使用一个循环，每次从opts中取出一个两元组，赋给两个变量。o保存选项参数，a为附加参数。接着对取出的选项参数进行处理。
"""

