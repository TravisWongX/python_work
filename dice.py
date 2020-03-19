from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        number = randint(1, self.sides)
        print(str(number))

        
while True:
    sides = input("Please enter a number: ")
    if sides == 'n' or sides == 'N':
        break
    else:
        dice = Die(int(sides))
        for i in range(0,10):
            dice.roll_die()

