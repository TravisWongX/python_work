1. 字符串换行拼接报错，在print()内不会
```python
name = 'alber' +   # 报错
       'einstein'
print('alber' +    # 不报错
       'einstein')

```

2. for loop的变量名
```python
foods = ("egg", "steak", "stew", "potato", "cumin")
for foods in foods:  # 这样也能正常执行
    print(foods)
```

3. 字典里可以有同名的键，最后一个有效？
```python
alien_0 = {'color': 'green', 'points': 5, 'color': 'red'}
alien_0['color'] # red
```
