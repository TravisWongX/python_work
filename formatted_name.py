def get_formatted_name(first_name, last_name, middle_name=''): # 让中间名可选
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title() # 返回值

musician = get_formatted_name('jimi', 'hendrix') # 将函数返回值赋给变量
print(musician)

musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)