from restaurant import Restaurant

restaurant = Restaurant('LaiFu', 'Chinese Food')
print(restaurant.number_served)
restaurant.set_number_served(2000)
print(restaurant.number_served)
restaurant.increment_number_served(500)
print(restaurant.number_served)