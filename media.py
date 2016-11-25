#Class movie creates the data structure to store the movies and its title,storyline,
#poster image, trailer url, movie director, and stars

import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_director, movie_releasedate, movie_stars):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.release_date = movie_releasedate
        self.stars = movie_stars

    #Launch the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    
