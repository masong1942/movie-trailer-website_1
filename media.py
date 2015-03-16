''' The custom media classes availble. 
    At present, only one - the Movie class
'''

import webbrowser

class Movie():
    '''A class for creating a movie object.
	   A class variable containing rating constants
       Instance variables of a movie: title, storyline, image url, preview trailer
       An Instance method to play the trailer '''	   
	   
    def __init__(self,title,storyline,poster,trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
		
    def show_trailer(self):
	    webbrowser.open(self.trailer_youtube_url)
		