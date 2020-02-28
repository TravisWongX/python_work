for value in range(1,21):
    print(value)

million = []
for value in range(1, 1000001):
    million.append(value)

# print(million)
print(min(million))
print(max(million))
print(sum(million))

odd_number = list(value for value in range(1,20,2))
for value in odd_number:
    print(value)

three_times = []
for value in range(3,31,3):
    three_times.append(value)
print(three_times)

cubes = list(value**3 for value in range(1,10))
for value in cubes:
    print(value)
