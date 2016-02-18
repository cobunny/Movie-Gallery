import fresh_tomatoes
import media

# Create each movie instance from the class Movie.
# Store data movie title, postURL and a YouTube link to the movie trailer.
the_revenant = media.Movie("The Revenant",
                           "http://goo.gl/GpyWou",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

amelie = media.Movie("Amelie",
                     "https://goo.gl/I0nYFg",
                     "https://www.youtube.com/watch?v=lrlQR_KH_nw")

kung_fu_panda_3 = media.Movie("Kung Fu Panda 3",
                              "https://goo.gl/IY0SXc",
                              "https://www.youtube.com/watch?v=10r9ozshGVE")

# Put each movie instance in the movies list.
movies = [the_revenant, amelie, kung_fu_panda_3]


# Pass movie list in open_movies_page.
# Generate a website from the movie list.
fresh_tomatoes.open_movies_page(movies)
