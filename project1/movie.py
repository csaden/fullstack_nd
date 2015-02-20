class Movie(object):
	"""A movie object that holds data about a movie"""

	def __init__(self, title, trailer_youtube_url, poster_image_url, imdb_rating, release_year, date, time, my_rating=0):
		"""Args:
			title (str): title of the movie
			trailer_youtube_url (str): url to the movie's youtube trailer
			poster_image_url (str): url to the movie's poster hosted by IMDB
			imdb_rating (str): movie's rating on IMDB (from 0 to 10)
			release_year (str): year the movie was released
			date (str): date I saw the movie
			time (str): showtime when I saw the movie
			my_rating (int): my personal rating of the movie (from 0 to 10)
		"""
		self.title = title
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url
		self.imdb_rating = imdb_rating
		self.release_year = release_year
		self.date = date
		self.time = time
		self.my_rating = my_rating

	def getTitle(self):
		"""returns the title of the movie"""
		return self.title

	def getPoster(self):
		"""returns the url for the movie's poster image on IMDB"""
		return self.poster_image_url

	def getTrailer(self):
		"""returns the url for the movie's trailer on youtube"""
		return self.trailer_youtube_url

	def getImdbRating(self):
		"""returns the rating for the movie on IMDB"""
		return self.imdb_rating

	def getMyRating(self):
		"""returns my rating of the movie"""
		return self.my_rating

	def setRating(self, new_rating):
		"""sets my rating of the movie"""
		self.my_rating = new_rating