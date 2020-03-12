def sandwiches(*toppings):
    for topping in toppings:
        print(topping)

sandwiches('lettuce')
sandwiches('broccoli', 'lettuce')
sandwiches('pepperoni', 'broccoli', 'lettuce')