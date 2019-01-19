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