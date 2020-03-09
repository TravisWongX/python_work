prompt = "\nPlease enter a pizza topping."
while True:
    topping = input(prompt)

    if topping != 'quit':
        print("You'll add " + topping + " to your pizza.")
    else:
        break
