age = input("How old are you? ")
age = int(age)

if age <= 3:
    print("\nThe ticket is free.")
elif age <= 12:
    print("\nThe ticket is $10.")
else:
    print("\nThe ticket is $15.")

while 1:
    print("looping")