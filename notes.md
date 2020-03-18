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
# len同样可以计算字典的长度
```

- 循环
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician) # 缩进4空格不是必须的，缩进1个空格也不会报错
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # 缩进要与上一句保持一致

for value in range(1,6): # range()函数生成数字
    print(value)
# range(30)可以只给一个参数，表示
numbers = list(range(1,6)) # list()函数生成数字列表
print(numbers)
even_numbers = list(range(2,11,2)) # 第三个参数指定步长
print(even_numbers)

min(numbers) # min()函数求列表中最小值
max(numbers) # max()函数求列表中最大值
sum(numbers) # sum()函数求列表和

squares2 = [value**3 for value in range(1,11)] # 用列表解析创建数字列表
print(squares2)
```

- 切片slice
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 与函数 range() 一样， Python 在到达你指定的第二个索引前面的元素后停止
print(players[:4]) # 从索引0到索引3
print(players[2:]) # 从索引2到最后
print(players[-3:]) # 倒数3个

for player in players[:3]: # 遍历切片Looping through a slice
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # 复制列表/切片
# friend_foods = my_foods会指向同一个列表
```

- 元组 Tuple
```python
#  Python 将不能修改的值称为 不可变的 ，而不可变的列表被称为 元组Tuple

dimensions = (200, 50) # 定义
print(dimensions[0]) # 像列表一样访问
print(dimensions[-1])

# tuple不可以append, insert等修改操作

```

- 格式
> 每级缩进都使用四个空格, 不要用制表符
> 每行不超过 80 字符
> 要将程序的不同部分分开，可使用空行
> https://www.python.org/dev/peps/pep-0008/

- if
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # ==区分大小写
        print(car.upper())
    else:
        print(car.title())


banned_users = ['andrew', 'carolina', 'david']
'andrew' in banned_users # 判断是否在列表内
'dav' not in banned_users # 是否不在

if age < 4:
    price = 0 # 移到:后面也不会报错
elif age < 18: # elif
    price = 5
else:
    price = 10

requested_toppings = []
if requested_toppings: # 判断列表是否为空
    do something...

```

- 字典dictionary
> 理解字典后，你就能够更准确地为各种真实物体建模。
```python
alien_0 = {'color': 'green', 'points': 5} # 键-值对
print(alien_0['color']) # 通过键访问值
print(alien_0['points'])

alien_0 = {} # 空字典
alien_0['color'] = 'green' # 添加/修改新键值对
alien_0['points'] = 5

del alien_0['color'] # 删除指定的键

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # 分多行，最后一行逗号可加可不加
    }

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

for name, language in favorite_languages.items(): # 遍历键值对
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")

print(favorite_languages.items())  # items()方法得到键值对list
# dict_items([('jen', 'python'), ('sarah', 'c'), ('edward', 'ruby'), ('phil', 'python')])

for name in favorite_languages.keys(): # keys()方法遍历所有的键
    print(name.title())

for name in favorite_languages: # keys()方法可以省去，默认调用
    print(name.title())

for language in favorite_languages.values(): # values()访问字典的值
    print(language.title())

for language in set(favorite_languages.values()): # set()集合，每个值必须唯一
    print(language)


# 嵌套

aliens = []

for alien_number in range(30): # 创建30个相同的字典存储到列表中
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: # 打印前5个字典
    print(alien)
print('...')

print("Total number of aliens: " + str(len(aliens)))


pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese'], # 字典中存储列表
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")

for topping in pizza['toppings']: # 访问字典中的列表
    print("\t" + topping)

# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

- 用户输入
```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt) # 获取用户输入， 但得到的是字符串

height = input("How tall are you, in inches?")
height = int(height) # int()将字符串转为整数， 不能转换浮点数形式的字符串，如'23.523'


if number % 2 == 0: # % 求模运算，得余数
    print("\nThe number " + str(number) + " is even.")

# a multiple(倍数) of 10

```

- while()循环
```python
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False # 使用flag控制循环是否结束
    else:
        print(message)

# break退出当前循环
# continue 忽略余下代码

# 如果程序陷入无限循环，可按 Ctrl + C

# 在 for 循环中不应修改列表，否则将导致 Python 难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用 while 循环
```

- 函数
```python
def greet_user(username): # username 形参(parameter)
    """显示简单的问候语""" # 文档字符串(docstring) 描述函数用来做什么的
    print("Hello!")

greet_user('Jesse') # 调用函数 , 'Jesse' 实参(argument)


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 位置实参，按形参顺序赋值
describe_pet('hamster', 'harry') 

# 关键字实参，可任意顺序
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(animal_type, pet_name='dog'): # 给形参指定默认值, 必须放最后


def get_formatted_name(first_name, last_name, middle_name=''):
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

# 每个函数都应只负责一项具体的工作

magicians_temp = make_great(magicians[:]) # 实参传递list的副本


def make_pizza(*toppings): # 空元组，接受任意实参
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info): # **空字典，接受任意个关键字实参
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')

print(user_profile)


# 模块 是扩展名为 .py 的文件

import pizza2 # 导入整个module

pizza2.make_pizza(16, 'pepperoni') # 调用module里的函数
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza2 import make_pizza # 从module中导入指定的函数

make_pizza(16, 'pepperoni') # 不需要用.调用函数
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_0, function_1, function_2

from pizza2 import make_pizza as mp # 给导入的函数指定别名

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza2 as p # 给模块指定别名

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import * # 导入模块中的所有函数，慎重使用！会使函数相互覆盖

# 函数编写指南
# 1. 形参、实参中的等号两边不要有空格
def function_name(parameter_0, parameter_1='default value')
# 参数过多时，用两个tab(8个空格)缩进
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...


```

- 类
```python
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age): # 初始化属性attribute ， self是要调用自身， 后面是创建实例时要给值的形参
        """Initialize name and age attributes."""
        self.name = name # 以 self 为前缀的变量都可供类中的所有方法使用
        self.age = age

    def sit(self):  # 类中的函数称为 方法 method
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6) # 实例化

print("My dog's name is " + my_dog.name.title() + ".") # 访问属性
print("My dog is " + str(my_dog.age) + "years old.")

my_dog.sit() # 调用方法
my_dog.roll_over()



##### My First Class #####
class Restaurant():
    """A Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self,cuisine_type): # 给方法传递其他参数
        """Prints two pieces of information"""
        print("restaurant_name: " + self.restaurant_name)
        print("cuisine_type: " + cuisine_type) # 其他参数不加self

    def open_restaurant(self): # self不能省略
        """print a message"""
        print("The restaurant is open.")

dafu = Restaurant('DaFu', 'Chinese food')
dafu.describe_restaurant('SiChuan food')
dafu.open_restaurant()


    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = 'Jake' 
        self.make = make  # 有默认值的属性也可通过形参传值
        self.make = 'Jake' # 在这个位置会覆盖掉形参传来的值，虽然没什么意义
        self.model = model 
        self.year = year
        self.odometer_reading = 0  # 有默认值的属性可以不通过形参传值

my_new_car = Car('audi', 'a4', 2016)
my_new_car.odometer_reading = 200 # 给属性重新赋值

    def update_odometer(self, mileage): # 定义方法更改属性
        """  
        set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """  # """内可任意换行"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


```

- 继承 inheritance
> 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用 继承 。一个类 继承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为 父类 ，而新类称为 子类 。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

```python
class ElectricCar(Car): # 定义子类subclass/childclass
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # 调用父类(超类superclass)的__init__
        self.battery_size = 70 # 添加子类独有属性

    def describe_battery(self): # 添加子类独有方法,如果父类有同名方法，也可这样重新定义
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    


```
