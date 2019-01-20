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

