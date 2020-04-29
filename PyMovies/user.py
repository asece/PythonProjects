#  Last sanity check: 2020-04-29
from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def save_to_file(self):
        with open('{}.txt'.format(self.name), 'w') as f:
            f.write('\t\t' + self.name + '\n')
            for movie in self.movies:
                f.write('{}, {}, {}\n'.format(movie.name, movie.genre, str(movie.watched)))

    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         content = f.readlines()         # returns a list of lines!
    #         username = content[0]
    #         movies = []
    #         for line in content[1:]:
    #             movie_data = line.split(',')    #[name, genre, watched]
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True') )
    #
    #         user = cls(username)
    #         user.movies = movies
    #         return user

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched == True

        return user
