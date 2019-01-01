# ===========================================================
print('\n返回值')
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
# 在函数中，可使用return语句将值返回到调用函数的代码行。
# 返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
def get_formatted_name(first_name, last_name , middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

aaa = get_formatted_name('AAA', 'aa', 'middle')
bbb = get_formatted_name('BBB', 'bb')
ccc = get_formatted_name('CCC', 'cc', 'middle')
print(aaa)
print(bbb)
print(ccc)

# 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name , middle_name='' , age =''):
    person = {
        'first_name':first_name.title(),
        'last_name':last_name.title()
    }
    if middle_name:
        person['middle_name'] = middle_name.title()
    if age:
        person['age'] = age
    return person
            
ddd = build_person('DDD', 'dd', 'middle')
eee = build_person('EEE', 'ee')
fff = build_person('FFF', 'ff',age='18',middle_name='hhh')
print(ddd)
print(eee)
print(fff)

while True:
    print("\nPlease tell me your name:") 
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    m_name = input("Middle name: ")
    if m_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name ,m_name) 
    print("\nHello, " + formatted_name + "!")

