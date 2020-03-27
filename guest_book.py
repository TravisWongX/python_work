filename = "guest_book.txt"

while True:
    name = input("Enter your name: ")
    if name == 'n':
        break

    print("Hello, " + name)

    with open(filename, 'a', encoding='utf-8') as file_object:
        file_object.write(name + '\n')

with open(filename, encoding='utf-8') as file_object:
    # print(file_object.readlines())
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
