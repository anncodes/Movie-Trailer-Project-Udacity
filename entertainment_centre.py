import fresh_tomatoes
import media

#Instances of the class Movie
kickass = media.Movie("Kickass", "Dave Lizewski is an unnoticed high school student and comic book fan who one day decides to become a super-hero, even though he has no powers, training or meaningful reason to do so.",
                      "http://www.impawards.com/2010/posters/kickass_ver9_xlg.jpg","https://www.youtube.com/watch?v=rFpWpkxsVI8","Matthew Vaughn","2010", "Aaron Taylor-Johnson, Nicolas Cage, Chloe Moretz")


avatar = media.Movie("Avatar", "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "http://www.goldposter.com/wp-content/uploads/2015/05/Avatar_poster_goldposter_com_56.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY","James Cameron","2009"," Sam Worthington, Zoe Saldana, Sigourney Weaver")

kill_bill = media.Movie("Kill Bill", "The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.", "http://cdn.pastemagazine.com/www/blogs/lists/2003.jpg","https://www.youtube.com/watch?v=7kSuas6mRpk"," Quentin Tarantino","2003"," Uma Thurman, David Carradine, Daryl Hannah")

school_of_rock = media.Movie("School of Rock", "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.", "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc", "Richard Linklater","2003","Jack Black, Mike White, Joan Cusack")

kungfu_panda = media.Movie("Kung fu Panda", "Po and his friends fight to stop a peacock villain from conquering China with a deadly new weapon, but first the Dragon Warrior must come to terms with his past.", "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg",
                           "https://www.youtube.com/watch?v=PXi3Mv6KMzY","Jennifer Yuh","2011", "Jack Black, Ian McShane, Angelina Jolie")

hunger_games = media.Movie("Hunger Games", "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.","http://cdn.collider.com/wp-content/uploads/the-hunger-games-poster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8", "Gary Ross", "2012","Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth ")

#Array of movies
movies = [kickass, avatar, kill_bill, school_of_rock, kungfu_panda, hunger_games]

#Opening the movie trailer page
fresh_tomatoes.open_movies_page(movies)
