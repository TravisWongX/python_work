- 命令行运行python脚本
```
cd 到脚本文件夹
python 脚本名
```

- 3个想用python做的事
1. 搭建个人博客
2. 写个爬虫
3. 开发一个桌面程序

- 变量名
> 应使用小写的 Python 变量名。在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。name_length用下划线连接

- 建议
> 在做每个练习时，都编写一个独立的程序。保存每个程序时，使用符合标准 Python 约定的文件名：使用小写字母和下划线，如 simple_message.py 和 simple_messages.py 。

- 字符串
```python
# 字符串方法

name = "michaeL jordAn"
print(name.title()) # 首字母大写
print(name.upper()) # 大写
print(name.lower()) # 小写

# + 拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + ' ' + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

print("\t\n") # \t制表 \n换行
print('\'') # \' 单引号转义

name = "   pineapple  "
name.lstrip() # 去掉左边空格，但不会改变字符串本身
name.rstrip() # 去掉右边空格
name.strip() # 去掉两边空格
name = name.strip() # 只有重新赋值才会改变字符串
```

- 数字
```python
2 ** 3 # 乘方
0.2 + 0.1 # 0.30000000000000004
3 / 2 # 1.5 Python3中除法得浮点数

age = 23
message = "Happy " + str(age) + "rd Birthday!"
# str()将数字转为字符串，Python中数字不能直接与字符串拼接，JS可以
```

- 注释
```python
# 这是一行注释
# 注释用来说明这段代码的用途
# 注释可以备注你的名字和日期
```

- Python之禅
```Python
# 在解释器窗口输入,就可以看到Zen of Python
>>> import this

now is better than never
# 你可以将余生都用来学习 Python 和编程的纷繁难懂之处，但这样你什么项目都完不成。不要企图编写完美无缺的代码；先编写行之有效的代码，再决定是对其做进一步改进，还是转而去编写新代码。
```

- 列表list 
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
print(bicycles[0]) # 索引从0开始
print(bicycles[-1]) # 访问倒数第一个元素，-2则倒数第二个，以此类推

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati' # 修改元素
motorcycles.append('honda') # 末尾添加元素
motorcycles.insert(1, 'BMW') # 在指定位置插入元素，其他元素右移
del motorcycles[1] # 在指定位置删除元素
popped_motorcycle = motorcycles.pop() # 删除最后一个元素，并返回其值
popped_motorcycle2 = motorcycles.pop(1) # 删除指定元素，并返回其值 
too_expensive = 'ducati'
motorcycles.remove(too_expensive) # 按值删除，只删除第一个与值匹配的, 且区分大小写
# Python的变量名区分大小写

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 按字母顺序由小到大排, 会改变list本身
cars.sort(reverse=True) # 按字母顺序反向排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True)) # 用sorted函数，不会改变list本身
print(sorted(cars))
print(cars)

cars.reverse() # 反转列表
print(len(cars)) # 计算列表长度
```

- 循环
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician) # 缩进4空格不是必须的，缩进1个空格也不会报错
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # 缩进要与上一句保持一致
```

