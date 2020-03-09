prompt = "If you could visit one place in the world,"
prompt += "\nwhere would you go?(Press N to quit)"

while True:
    place = input(prompt)
    
    if place != 'N':
        print("You wanna go to " + place + ".")
    else:
        break