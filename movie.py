class Movie():
    '''This class stores movie info for display on the web.'''

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''
        This constructor for the Movie class takes four arguments which store
        info about the movie to display on the webpage.
            movie_title stores the movie's title.
            movie_storyline stores the movie's storyline but is unused.
            poster_image stores the URL for the poster image.
            trailer_youtube stores the URL for the movie's trailer.
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
