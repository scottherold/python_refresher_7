class Song:
    # DocString -- see PEP 257
    # DocStrings should always use triple quotes

    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artists): An artist object representing the song's creator
        duration (int): the duration of the song in seconds. May be zero.
    """
    
    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
            title(str): Initilizes the 'title' attribute
            artist (Artist): An Artist object representing the song's creator
            duration (Optional[int]): Initial value for the 'duration' attibute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration