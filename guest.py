name = input("Enter your name: ")

filename = "guest.txt"

with open(filename, 'w', encoding='utf8') as file_object:
    file_object.write(name)