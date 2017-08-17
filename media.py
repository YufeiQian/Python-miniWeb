class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Args:
        movie_title - string
        movie_storyline - string
        poster_image - string
        trailer_youtube - string
        """
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
