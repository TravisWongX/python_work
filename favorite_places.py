favorite_places = {
    'jerry': ['huangshan', 'lushan', 'huashan'],
    'tom': ['xian', 'luoyang', 'beijing'],
    'lucy': ['tokyo', 'sanya', 'beihaidao'],
    }

for name, places in favorite_places.items():
    print('\n' + name + ':')
    for place in places:
        print('\t' + place)