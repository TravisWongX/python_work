alien_color = 'red'
if alien_color == 'green':
    print("Kudos to you!You've earned 5 points.")
elif alien_color == 'purple':
    print("Kudos to you!You've earned 10 points.")
else:
    print("Whoops! Game over!")

age = 27
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

favorite_fruits =  ['banana', 'apple', 'orange', 'tomato']
if 'banana' in favorite_fruits:
    print("\nI really like bananas.")
if 'apple' in favorite_fruits:
    print("I really like apples.")
if 'water melon' not in favorite_fruits:
    print("Oh! I forgot water melon.")