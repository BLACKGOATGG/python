#======================================================
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "hello, " + full_name.title() + "!"
print(message)

#======================================================
age = 23
message = "Happy "+ str(age) + "rd Birthady!"
#在字符串中使用整数时，需要显式地指 出你希望Python将这个整数用作字符串
#message = "Happy "+ int(age) + "rd Birthady!"
print(message)
