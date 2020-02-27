cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 按字母顺序由小到大排
print(cars)
cars.sort(reverse=True) # 按字母顺序反向排序
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True)) # 用sorted函数，不会改变list本身
print(sorted(cars))
print(cars)

cars.reverse() # 反转列表
print(cars)

print(len(cars)) # 计算列表长度