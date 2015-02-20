import sys
from movie import Movie
import fresh_tomatoes as ft

def main(args=None):

	movies_list = []
	
	with open('movies.tsv', 'r') as movie_file:
		
		movies = movie_file.readlines()[1:]
		
		for row in movies:
			
			movie_data = row.split("\t")
			
			# create movie instance and unpack data using *
			movie = Movie(*movie_data)
			
			movies_list.append(movie)
	
	ft.open_movies_page(movies_list)

if __name__ == '__main__':
	sys.exit(main())