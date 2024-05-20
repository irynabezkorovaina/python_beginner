GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}

# CAST = {
#     'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
#     'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
#     'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
#     'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
#     'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
#     'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
# }

search_by_genre = input("Search by Genre (y/n): ")

while search_by_genre != 'y' and search_by_genre != 'n':
    print("Error: Invalid input. Please enter 'y' or 'n'")
    search_by_genre = input("Search by Genre (y/n): ")

if search_by_genre == 'y':
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre:")

    while genre not in GENRES:
        print(f"Genre {genre} not found. Please try again.")
        genre = input("Enter genre:")

    print("Available Movies:", GENRES[genre])
    movie = input("Enter movie: ")

    while movie not in GENRES[genre]:
        print(f"Movie {movie} not found. Please try again.")
        movie = input("Enter movie: ")

    print(f"Movie to watch: {movie}. Genre: {genre}.")

elif search_by_genre == 'n':
    search_by_actor = input("Search by Actors (y/n): ")

    while search_by_actor != 'y' and search_by_actor != 'n':
        print("Error: Invalid input. Please enter 'y' or 'n'")
        search_by_actor = input("Search by Actors (y/n): ")

    if search_by_actor == 'y':
        print("Available Actors:", list(ACTORS.keys()))
        actor = input("Enter actor: ")

        while actor not in ACTORS:
            print(f"Error: Actor {actor} not found. Please try again.")
            actor = input("Enter actor: ")
        print("Available movies:", ACTORS[actor])
        movie = input("Enter movie: ")

        while movie not in ACTORS[actor]:
            print(f"Error: Movie {movie} not found. Please try again.")
            movie = input("Enter movie: ")
        print(f"Movie to watch: {movie}. Starring: {actor}.")

    elif search_by_actor == 'n':
        print("Error: Request has ended.")

#         if search_by_actor == 'y':
#         print("Available Actors:")
#         list_of_actors = []
#         for actors_list in CAST.values():
#             for actor in actors_list:
#                 if actor not in list_of_actors:
#                     list_of_actors.append(actor)
#         print(list_of_actors)
#         actor = input("Enter actor: ")
#         movies_list = []
#         for movie, cast in CAST.items():
#             if actor in cast:
#                 movies_list.append(movie)
#         if movies_list:
#             print("Available movies:", movies_list)
#             movie = input("Enter movie: ")
#             if movie in movies_list:
#                 print(f"Movie to watch: {movie}. Starring: {actor}.")
#             else:
#                 print("Error: Movie is not found.")
#         else:
#             print("Error: Actor is not found.")
#     elif search_by_actor == 'n':
#         print("Error: Request has ended")
#     else:
#         print("Error: You must select a valid option for searching by actor.")
# else:
#     print("Error: You must select a valid option for searching by genre.")


#         print("Available Actors:", list(ACTORS.keys()))
#         actor = input("Enter actor: ")
#         if actor in ACTORS:
#             print("Available movies: ", ACTORS[actor])
#             movie = input("Enter movie: ")
#             if movie in ACTORS[actor]:
#                 print(f"Movie to watch: {movie}. Starring: {actor}.")
#             else:
#                 print("Error: Movie is not found.")
#         else:
#             print("Error: Actor is not found.")
#     elif search_by_actor == 'n':
#         print("Error: Request has ended")
#     else:
#         print("Error: You must select a valid option for searching by actor.")
# else:
#     print("Error: You must select a valid option for searching by genre.")
