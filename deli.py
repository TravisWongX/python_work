sandwich_orders = ['cucumber', 'pastrami','brocoli', 'pepperoni','pastrami', 'lettuce','pastrami', 'pettals', 'algae']
finished_sandwiches = []

print("We have run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your " + finished_sandwich + " sandwich.")

    finished_sandwiches.append(finished_sandwich)

print("\nWe have made this sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)