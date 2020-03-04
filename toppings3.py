availbale_toppings = ('mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availbale_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")