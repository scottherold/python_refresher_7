class Song:
    # DocString -- see PEP 257
    # DocStrings should always use triple quotes
    # DocStrings provide 'help' when the class is passed into the help()
    # function

    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artists): An artist object representing the song's creator
        duration (int): the duration of the song in seconds. May be zero.
    """
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist responsibile for the album. If not 
            specified, the artist will default to "Various Artists"
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's tracks
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list.
        
        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will added to that
                position in tracks - inserting it between other songs if 
                necessary. Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist. The list 
            includes only those albums in this collection, it is not an
            exhaustive list of the artist's publish albums.
            
    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list. If the album is 
                already present, it will not be added again (although this is
                yet to implemented)
        """
        self.albums.append(album)

# Bootstrap data from .txt file
def load_data():
    new_artist = None
    new_ablum = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consists of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            
            # mapping data from unpacked tuple
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

# Execute only if the program is run as a script
if __name__ == '__main__':
    load_data()