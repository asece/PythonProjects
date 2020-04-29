#  Last sanity check: 2020-04-29
import json
import os

from movie import Movie
from user import User


#
# with open('my_file.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())

def menu():
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)


    user_input = input("Enter: \n\t'a' to add a movie\n"
                          "\t's' to see the list of movies\n"
                          "\t'w' to set a movie as watched\n"
                          "\t'd' to delete a movie\n"
                          "\t'l' to to see the list of watched movies\n"
                          "\t'q' to save and quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter movie name: ")
            movie_genre = input("Enter movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name:  {} Genre:  {} Watched:  {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter movie to set watched: ")
            user.delete_movie(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter movie to delete: ")
            user.set_wathced(movie_name)
        elif user_input == 'l':
            for movie in user.movies:
                print("Name:  {} Genre:  {} Watched:  {}".format(movie.name, movie.genre, movie.watched))
        user_input = input("Enter: \n\t'a' to add a movie\n"
                          "\t's' to see the list of movies\n"
                          "\t'w' to set a movie as watched\n"
                          "\t'd' to delete a movie\n"
                          "\t'l' to to see the list of watched movies\n"
                          "\t'q' to save and quit")

    with open(filename, 'w') as f:
        json.dump(user.json(), f)

def file_exists(filename):
    return os.path.isfile(filename)

menu()