prompt = "Please enter a number,"
prompt += "\nI'll tell you if it is a multiple of 10 or not."

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(str(number) + ' is a multiple of 10.')
else:
    print(str(number) + ' is not a multiple of 10.')