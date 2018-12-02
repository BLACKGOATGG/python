#======================================================
#列表解析
#列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [i for i in range(0,10)];
print(squares);

squares_2 = list(range(0,10));
print(squares_2)

#练习
#一百万：创建一个列表，其中包含数字 1~1 000 000，再使用 min()和 max()核实该列表确实是从 1 开始，到 1 000 000 结束的。另外，对这个列表调 用函数 sum()，看看 Python 将一百万个数字相加需要多长时间。
yibaiwan=list(range(1,1000001));
#print(yibaiwan);
print(min(yibaiwan));
print(max(yibaiwan));
print(sum(yibaiwan));

#奇数:通过给函数 range()指定第三个参数来创建一个列表，其中包含 1~20 的 奇数;再使用一个 for 循环将这些数字都打印出来。
jishu = [ i for i in range(1,21,2) ];
print(jishu);

#3 的倍数:创建一个列表，其中包含 3~30 内能被 3 整除的数字;再使用一个 for 循环将这个列表中的数字都打印出来。
sanbeishu = [ i for i in range(3,30,3)];
for i in sanbeishu:
	print(i);

#立方解析:使用列表解析生成一个列表，其中包含前 10 个整数的立方。
lifang = [ i**3  for i in range(1,11)];
print(lifang);
