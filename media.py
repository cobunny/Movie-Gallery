import webbrowser


class Movie:
    """
        Create a Movie class with instance variables, an instance method.
    """

    # valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """
            Create variables to store movie title, poster image URL and YouTube trailer URL
        """

        # Instance variable - title
        self.title = movie_title

        # Instance variable - poster_image_url
        self.poster_image_url = poster_image

        # Instance variable - trailer_youtube_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
            Open trailer URL in a web browser.
        """

        # Instance method - Calling open() method from module webbrower

        webbrowser.open(self.trailer_youtube_url)
