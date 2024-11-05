#!/usr/bin/env python3

def make_album(artist_name, album):
    """A function that creates a dictionary of an album and the artist"""

    my_list = {'musician': artist_name, 'album_name': album}
    return my_list

while True:
    print("\nEnter Favorite Musician name and Album")
    print("(To quit prompt enter 'q')")

    name = input("Name: ")
    if name == 'q':
        break
    title = input("Album: ")
    if title == 'q':
        break

    favorite_musician = make_album(name.title(), title.title())

    print("\nMy favorite artist and one of their albums {}".format(favorite_musician))
