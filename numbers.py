for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

print("Min: " + str(min(squares)))
print("max: " + str(max(squares)))
print("sum: " + str(sum(squares)))

squares2 = [value**3 for value in range(1,11)]
print(squares2)