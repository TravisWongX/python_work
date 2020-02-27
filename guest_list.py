guests = ['Avril', 'Bruce Lee', '秦始皇', '孔子']
message0 = "Hi " + guests[0].title() + ", would you like to come in for dinner?" 
message1 = "Hi " + guests[1].title() + ", would you like to come in for dinner?" 
message2 = "Hi " + guests[2].title() + ", would you like to come in for dinner?" 
message3 = "Hi " + guests[3].title() + ", would you like to come in for dinner?" 
print(message0)
print(message1)
print(message2)
print(message3)

busy_guy = guests.pop(3)
message = "Sorry, " + busy_guy + " won't come."
print(message)
guests.append("Michael Jacson")
print(guests)
print("Hooray, I've found a much bigger dining table.")
guests.insert(0, 'kobe bryant')
guests.insert(2, 'Madonna')
guests.append('Tesla')
print("our new guests will be " + str(guests))

print("Sorry! Bad news! I can invite only two guests to dinner...")
guy_popped = guests.pop()
print("Goodbye " + guy_popped.title())
guy_popped = guests.pop(1)
print("Goodbye " + guy_popped.title())
guy_popped = guests.pop(2)
print("Goodbye " + guy_popped.title())
guy_popped = guests.pop(0)
print("Goodbye " + guy_popped.title())
guy_popped = guests.pop()
print("Goodbye " + guy_popped.title())
print(guests)
print("Kudos to " + guests[0].title() + ' and ' + guests[-1].title() +
      ", Welcome to our dinner.")

del guests[-1]
del guests[-1]
print(guests)