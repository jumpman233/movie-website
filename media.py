import webbrowser


class Movie():
    """ a dataset about a movie

    A Movie instance contains attributes about a movie, like movie_title,
    movie_storyline, etc.
    It will be used to build a movie website

    Attributes:
        title: a string about the title of the movie.
        storyline: a string about the storyline of the movie.
        poster_image_url: a string about a url of the poster of the movie.
        trailer_youtube_url: a string about a url of the trailer in youtube.
        label: a string represents the movie type.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, label):
        """inits the Movie class with movie_title, movie_storyline, poster_image,
        trailer_youtube, label"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.label = label

    def show_trailer(self):
        """open the youtube url in the webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
