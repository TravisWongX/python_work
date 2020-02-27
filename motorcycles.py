motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # 修改元素
print(motorcycles)

motorcycles.append('honda') # 末尾添加元素
print(motorcycles)

motorcycles.insert(1, 'BMW') # 在指定位置插入元素，其他元素右移
print(motorcycles)

del motorcycles[1] # 在指定位置删除元素
print(motorcycles)

popped_motorcycle = motorcycles.pop() # 删除最后一个元素，并返回其值
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle2 = motorcycles.pop(1) # 删除指定元素，并返回其值
print(motorcycles)
print(popped_motorcycle2)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # 按值删除
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.remove(too_expensive)
print(motorcycles)