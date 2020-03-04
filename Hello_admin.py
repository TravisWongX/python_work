usernames = ['admin', 'Eric', 'lucky', 'jacy']
# usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, Would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users.")

current_users = ['hippo', 'rhino', 'goose', 'Eric', 'rose']
new_users = ['Jack', 'Hippo', 'GOOSE', 'raccoon', 'giraffe']

current_users_lower = []
for username in current_users:
    current_users_lower.append(username.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print("Sorry, " + user + " is not available.")
    else:
        print("Kudos to you, " + user + " is available.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number) + 'th')