def make_great(magicians):
    magicians_temp = []
    while magicians:
        magician = magicians.pop()
        magician = 'Great to each ' + magician
        magicians_temp.append(magician)
    return magicians_temp


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['andy', 'jelly', 'patric', 'squid']

magicians_temp = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_temp)