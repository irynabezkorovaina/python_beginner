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

search_by_genre = input("Search by Genre (y/n): ")
if search_by_genre == 'y':
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre:")
    if genre in GENRES:
        print("Available Movies:", GENRES[genre])
        movie = input("Enter movie: ")
        if movie in GENRES[genre]:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print("Error: Movie is not found.")
    else:
        print("Error: Genre is not found.")
elif search_by_genre == 'n':
    search_by_actor = input("Search by Actors (y/n): ")
    if search_by_actor == 'y':
        print("Available Actors:", list(ACTORS.keys()))
        actor = input("Enter actor: ")
        if actor in ACTORS:
            print("Available movies: ", ACTORS[actor])
            movie = input("Enter movie: ")
            if movie in ACTORS[actor]:
                print(f"Movie to watch: {movie}. Starring: {actor}.")
            else:
                print("Error: Movie is not found.")
        else:
            print("Error: Actor is not found.")
    elif search_by_actor == 'n':
        print("Error: Request has ended")
    else:
        print("Error: You must select a valid option for searching by actor.")
else:
    print("Error: You must select a valid option for searching by genre.")
