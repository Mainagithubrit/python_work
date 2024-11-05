#!/usr/bin/env python3

def make_album(artist_name, album, songs=None):
    """A function that creates a dictionary of an album and the artist"""

    my_list = {'musician': artist_name.title(), 'album_name': album.title()}

    if songs:
       my_list['songs'] = songs

    return my_list

favorite_musician = make_album('linkin park', 'hybrid theory')
print(favorite_musician)

favorite_musician = make_album('linkin park', 'meteora')
print(favorite_musician)

favorite_musician = make_album('linkin park', 'one more light', songs=10)
print(favorite_musician)
