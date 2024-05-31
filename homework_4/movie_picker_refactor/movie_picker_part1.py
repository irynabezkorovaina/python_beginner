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

# Main program
search_by_genre = input("Search by Genre (y/n): ")

while search_by_genre != 'y' and search_by_genre != 'n':
    print("Error: Invalid input. Please enter 'y' or 'n'")
    search_by_genre = input("Search by Genre (y/n): ")

if search_by_genre == 'y':
    genre = search(source=list(GENRES.keys()), source_name='genre')
    movie = search(source=GENRES[genre], source_name='movie')
    print(f"Movie to watch: {movie}. Genre: {genre}.")
else:
    search_by_actor = input("Search by Actors (y/n): ")
    while search_by_actor != 'y' and search_by_actor != 'n':
        print("Error: Invalid input. Please enter 'y' or 'n'")
        search_by_actor = input("Search by Actors (y/n): ")

    if search_by_actor == 'y':
        actors_list = movies_by_actors(CAST)
        actor = search(source=list(actors_list.keys()), source_name='actor')
        movie = search(source=actors_list[actor], source_name='movie')
        print(f"Movie to watch: {movie}. Starring: {actor}.")
    else:
        print("Error: Request has ended.")
