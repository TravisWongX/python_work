def make_album(artist, album, tracks=0):
    if tracks:
        albums = {'aritst': artist, 'album': album, 'tracks': tracks}
    else:
        albums = {'aritst': artist, 'album': album}
    print(albums)

make_album('tod', 'sky', 16)
make_album('jerk', 'see')
