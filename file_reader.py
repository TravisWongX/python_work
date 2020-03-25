filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # 是一个列表
    # lines = file_object.readline() # readline 是逐个读字符

for line in lines:
    print(line.rstrip())