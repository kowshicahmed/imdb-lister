from imdb import Cinemagoer
import re
import pandas as pd


def get_ratings(movie_list):
    # create an instance of the Cinemagoer class
    ia = Cinemagoer()
    movie_names = []
    movies_ratings = []

    with open(movie_list) as movie_list:
        for movie in movie_list:
            movie = re.sub("\s+", ' ', movie).strip()  # Remove whitespaces new lines and tabs
            try:
                movies = ia.search_movie(movie)
            except:
                movies = ia.search_movie(movie.split('(')[0])   # Search again by removing year, it was giving error
            top_match = ia.get_movie(movies[0].movieID, info=['main'])
            movie_names.append(movie)
            movies_ratings.append(top_match.get('rating'))

    df = pd.DataFrame(list(zip(movie_names, movies_ratings)),
                      columns=['Name', 'Rating'])
    df = df.sort_values(by=['Rating'], ascending=False)
    df.to_excel('movie-ratings.xlsx')


if __name__ == '__main__':
    movie_list_file = 'movie-list.txt'
    get_ratings(movie_list_file)
    pass