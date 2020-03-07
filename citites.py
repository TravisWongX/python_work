cities = {
    'beijing': {'country': 'China', 'population': 21540000, 'fact': 'bbbbb'},
    'london': {'country': 'England', 'population': 13324324, 'fact': 'LLLLL'},
    'paris': {'country': 'Franch', 'population': 2323442, 'fact': 'PPPP'},
}

for name, city in cities.items():
    print('\n' + name + ':')
    for key, value in city.items():
        print('\t' + key + ': ' + str(value))