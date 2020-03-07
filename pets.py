tom = {'kind': 'cat', 'owner': 'Mr. Jon'}
jerry = {'kind': 'mouse', 'owner': 'Mr. king'}
jungle = {'kind': 'lizard', 'owner': 'Mr. Pan'}
pets = (tom, jerry, jungle)

for pet in pets:
    print(pet['kind'])
    print(pet['owner'])