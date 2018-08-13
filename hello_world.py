# -*- coding: UTF-8 -*-
hello = "hello world!"
print(hello)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:print(n, '是一个素数')
        
            

# print hello.decode("utf-8").encode("gbk");
