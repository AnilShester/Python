def display_message():
    print("We are learning about python in this chapter.")

display_message()


def favorite_book(title):
    print(f"One of my favorite book is {title.title()}")

favorite_book("lord of the rings")

def make_shirt(size = "large", message = "I love python"):
    print(f"The shirt that you want is if size {size} and has {message} printed on it.")

make_shirt("medium", "You will never walk alone")
make_shirt()


def city_country(name, country):
    return (f" \"{name}, {country}\"")

city1 = city_country("Lalitpur", "Nepal")
print(city1)


def make_album(artist, album_title, tracks_number = 0):
    if tracks_number <= 0:
        return {
        'artist': artist,
        'album': album_title
        }
    else:
        return{
            'artist': artist,
            'album': album_title,
            'total_tracks': tracks_number
        }

    print("Enter artist and album name")
    print("enter q to quit")
while True:
    artist = input("Enter the name of the artist")
    if artist == 'q':
        break;
    album = input("Enter the name of the album")
    if artist == 'q':
        break;

    album1 = make_album(artist, album, 8)
    
    print(album1)
    