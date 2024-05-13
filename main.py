
def display_menu():
    print("""
The Movie List program
COMMAND MENU
list - List all movies
add  - Add a movie
del  - Delete a movie
exit - Exit program
""")


def get_movies_from_file(filepath):
    movies = []
    with open(filepath, 'r') as file:
        movies = [line.strip() for line in file]
    return movies


def display_movies(movies):
    print("Movie list")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")


def add_movie(movies, title, filepath):
    movies.append(title)
    write_movies_to_file(filepath, movies)
    print(f"Movie: {title} was added.")


def delete_movie(movies, number, filepath):
    if 0 < number <= len(movies):
        removed_movie = movies.pop(number - 1)
        write_movies_to_file(filepath, movies)
        print(f"Movie: {removed_movie} was deleted.")
    else:
        print("Invalid movie number.")


def write_movies_to_file(filepath, movies):
    with open(filepath, 'w') as file:
        for movie in movies:
            file.write(movie + '\n')


def main():
    filepath = 'movies.txt'  
    movies = get_movies_from_file(filepath)
    display_menu()
    while True:  
        command = input("Command: ")
        if command.lower() == 'list':
            display_movies(movies)
        elif command.lower() == 'add':
            title = input("Movie: ")
            add_movie(movies, title, filepath)
            display_movies(movies)
        elif command.lower() == 'del':
            try:
                number = int(input("Number: "))
                delete_movie(movies, number, filepath)
                display_movies(movies)
            except ValueError:
                print("Invalid number. Please try again.")
        elif command.lower() == 'exit':
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
