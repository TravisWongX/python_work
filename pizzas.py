pizzas = ['New York Style', 'Chicago Style', 'Pan Pizza', 'Thick style']

print("The first three items in the list are:")
for item in pizzas[0:3]:
    print(item)

print("\nThree items from the middle of the list are:")
for item in pizzas[1:4]:
    print(item)

print("\nThe last three items in the list are:")
for item in pizzas[-3:]:
    print(item)

friend_pizzas = pizzas[:]
pizzas.append("Take and Bake Style")
friend_pizzas.append("Cracker and Thin Styles")

print("\nMy favorite pizzas are:")
for item in pizzas:
    print(item)

print("\nMy friend's favorite pizzas are:")
for item in friend_pizzas:
    print(item)