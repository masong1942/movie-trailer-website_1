''' 
Creates a list of Movie objects for my favorite movies, 
and then calls the open_movies_page function of the fresh_tomatoes module
giving it the movie list. 

That function will generate a web page (fresh_tomates.html) and load it into
a browser to be viewed. 
'''

import media, fresh_tomatoes

the_missing = media.Movie(
    "The Missing",
    "In the early West, a man gone Apache, returns home after a decade,to rescue his kidnapped grandaughter.",
    "http://images.moviepostershop.com/the-missing-movie-poster-2003-1020249250.jpg",
    "https://www.youtube.com/watch?v=535RNQ0REx8"
)

the_unforgiven = media.Movie(
    "The Unforgiven",
    "A Retired Old West gunslinger reluctantly takes on one last job, " \
        "with the help of his old partner and a young man." , 
    "http://ia.media-imdb.com/images/M/" \
        "MV5BMTkzNTc0NDc4OF5BMl5BanBnXkFtZTcwNTY1ODg3OA@@._V1_SY317_CR5,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=XDAXGILEdro"
)

hombre = media.Movie(
  "Hombre",
  "An Apache-raised white man, learns of an inheritance from his father, which includes a boarding " \
     "house. He decides to sell the bording house and buy a herd of horses as repayment to the " \
     "Apache for his rearing and hunting on their land. A stage out of town, a corrupt indian " \
     "agent carrying embezzled funds, an attempted stage robbery and the robbers persuit of " \
     "Hombre are the saga of this file." , 
  "http://troychafin.com/wp-content/uploads/2009/07/hombre-title-still-515x386.jpg",
  "https://www.youtube.com/watch?v=GOwkV_E1Y7I"
)	 

man_on_fire = media.Movie(
  "Man on Fire",
  "In Mexico City, a former American assassin swears vengeance on those who kidnapped " \
      "the daughter of the family he was hired to protect."  ,  
  "http://www.impawards.com/2004/posters/man_on_fire.jpg",
  "https://www.youtube.com/watch?v=g4kLizDXLY0"
)

valley_of_elah = media.Movie(
  "In the Valley of Elah",
  "A veteran father searches for his military son and, after finding his body, " \
      " hunts for his son's killers. He then discovers one  of his son's demons " \
	  " of war" ,
  "http://upload.wikimedia.org/wikipedia/en/thumb/0/0a/In_the_valley_of_elah.jpg" \
      "/220px-In_the_valley_of_elah.jpg",
  "https://www.youtube.com/watch?v=1EwmvAEetTs"
)
	
last_mohicans = media.Movie(
  "The Last of the Mohicans",
  "The last of the once great Mohican tribe, is lead to slaughter by "  \
     "the Army who is relocating them, having been betrayed by by their " \
	 "Huron scout", 
  "https://encrypted-tbn0.gstatic.com/images" \
    "?q=tbn:ANd9GcTZozSONVo2O_5anP-US4wXoCRC95nmK9jLqSwZQeOVuYFomSmhSw" ,
  "https://www.youtube.com/watch?v=DcJA22mXBEk"
)

movies = [the_missing,the_unforgiven,hombre,last_mohicans,man_on_fire,valley_of_elah]
fresh_tomatoes.open_movies_page(movies)
