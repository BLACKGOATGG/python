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

