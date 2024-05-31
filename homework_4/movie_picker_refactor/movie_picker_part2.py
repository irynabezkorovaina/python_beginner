def search(source, source_name='genre'):
    print(f'Available {source_name}(s): {source}')
    source_input = input(f"Enter {source_name} : ")
    while source_input not in source:
        print(f"Error: {source_name} {source_input} not found. Please try again")
        source_input = input(f"Enter {source_name} : ")
    return source_input


def movies_by_actors(cast):
    actors_list = {}
    for movie, cast_list in cast.items():
        for actor in cast_list:
            if actor not in actors_list:
                actors_list[actor] = []
            actors_list[actor].append(movie)
    return actors_list


def prepare(genres, pg_rate):
    new_genres = {}
    for age, movies in pg_rate.items():
        new_genres[age] = {movie for movie in genres if all(movie in movies for movie in genres[movie])}
    return new_genres


GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}

age = None
while age is None:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Error: Please enter an integer.")

if age < 13:
    print("You are too young to watch any movies.")
else:
    available_movies = [movie for age_req, movies in PG.items() for movie in movies if age >= age_req]

    search_by_genre = input("Search by Genre (y/n): ")

    while search_by_genre != 'y' and search_by_genre != 'n':
        print("Error: Invalid input. Please enter 'y' or 'n'")
        search_by_genre = input("Search by Genre (y/n): ")

    if search_by_genre == 'y':
        genre = search(source=list(GENRES.keys()), source_name='genre')
        available_movies_for_genre = [movie for movie in GENRES.get(genre, []) if movie in available_movies]
        if not available_movies_for_genre:
            print("Error: There are no movies of this genre available for your age.")
        else:
            movie = search(source=available_movies_for_genre, source_name='movie')
            print(f"Movie to watch: {movie}. Genre: {genre}.")
    else:
        search_by_actor = input("Search by Actors (y/n): ")
        while search_by_actor != 'y' and search_by_actor != 'n':
            print("Error: Invalid input. Please enter 'y' or 'n'")
            search_by_actor = input("Search by Actors (y/n): ")

        if search_by_actor == 'y':
            actors_list = movies_by_actors(CAST)
            actor = search(source=list(actors_list.keys()), source_name='actor')
            available_movies_for_actor = [movie for movie in actors_list.get(actor, []) if movie in available_movies]
            if not available_movies_for_actor:
                print("Error: There are no movies with this actor available for your age.")
            else:
                movie = search(source=available_movies_for_actor, source_name='movie')
                print(f"Movie to watch: {movie}. Starring: {actor}.")
        else:
            print("Error: Request has ended.")
