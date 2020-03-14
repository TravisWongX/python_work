class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):  # 初始化属性， self是要调用自身， 后面是创建实例时要给值的形参
        """Initialize name and age attributes."""
        self.name = name # 以 self 为前缀的变量都可供类中的所有方法使用
        self.age = age

    def sit(self): # 定义方法
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
yong_dog = Dog('mini', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()


print("My dog's name is " + yong_dog.name.title() + ".")
print("My dog is " + str(yong_dog.age) + " years old.")

yong_dog.sit()
yong_dog.roll_over()