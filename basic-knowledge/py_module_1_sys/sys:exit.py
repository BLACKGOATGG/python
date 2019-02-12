# python中 os._exit() 和 sys.exit(), exit(0)和exit(1) 的用法和区别

"""
    Python的程序有两中退出方式：os._exit()， sys.exit()。本文介绍这两种方式的区别和选择。

    os._exit()会直接将python程序终止，之后的所有代码都不会继续执行。

    sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。
    如果有捕获此异常的代码，那么这些代码还是会执行。捕获这个异常可以做一些额外的清理工作。
    0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。
"""

# 举例说明
# import os
# try:
#     os._exit(0)
# except:
#     print('die')
# 此处不会打出”die”


import sys
try:
    sys.exit(0)
except:
    print('die')
finally:
    print('cleanup')
# 输出：
# die
# cleanup

"""
    综上，
    os._exit()直接将python解释器退出，余下的语句不会执行。
    sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作。

    一般情况下使用sys.exit()即可，一般在fork出来的子进程中使用os._exit()

    一般来说os._exit() 用于在线程中退出 
    sys.exit() 用于在主线程中退出。

    exit() 跟 C 语言等其他语言的 exit() 应该是一样的。 
    os._exit() 调用 C 语言的 _exit() 函数。

    builtin.exit 是一个 Quitter 对象，这个对象的 call 方法会抛出一个 SystemExit 异常。
"""

# exit(0)和exit(1)的区别
""" 
    exit(0)：无错误退出 
    exit(1)：有错误退出 
    退出代码是告诉解释器的（或操作系统
"""