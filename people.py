people = [
    {'name': 'Jack', 'age': 27, 'city': 'New York'},
    {'name': 'Lucy', 'age': 18, 'city': 'San Francisco'},
    {'name': 'Mei', 'age': 20, 'city': 'Chicago'},
    ]

for person in people:
    print("name: " + person['name'])
    print("age: " + str(person['age']))
    print("city: " + person['city'] + "\n")
