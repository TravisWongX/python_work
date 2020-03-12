def build_profile(first, last, **user_info):
    print("first name: " + first.title())
    print("last name: " + last.title())
    for key,value in user_info.items():
        print(key + ": " + str(value))

build_profile('eric', 'long', age = 18, city='New York')