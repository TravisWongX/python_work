def city_country(name, country):
    print("\"" + name.title() + ", " + country.title() + "\"\n")

while True:
    print("Please enter city and country")
    print("enter 'q' at any time to quit")

    name = input("Please enter the city: ")
    if name == 'q':
        break

    country = input("Please enter the country: ")
    if country == 'q':
        break

    city_country(name, country)
