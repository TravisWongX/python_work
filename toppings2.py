# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are fresh out of green right now.")
        else:
            print("Adding " + requested_topping + ".")
else: 
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")


#if 'mushrooms' in requested_toppings:
 #   print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
  #  print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
 #   print("Adding extra cheese")

# print("\nFinished making your pizza!")
