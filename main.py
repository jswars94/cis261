# James Alan Bush (SU200619708)
# CIS261
# Week 6 - Lab Assigment - Movie Guide Part 2

# Function to display the menu
def display_menu():
    print("""
The Movie List program
COMMAND MENU
list - List all movies
add  - Add a movie
del  - Delete a movie
exit - Exit program
""")

# Function to read movie titles into a list from a file
def get_movies_from_file(filepath):
    movies = []
    with open(filepath, 'r') as file:
        movies = [line.strip() for line in file]
    return movies

# Function to display all movie titles
def display_movies(movies):
    print("Movie list")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")

# Function to add a movie title to the list and file
def add_movie(movies, title, filepath):
    movies.append(title)
    write_movies_to_file(filepath, movies)
    print(f"Movie: {title} was added.")

# Function to delete a movie title from the list and file
def delete_movie(movies, number, filepath):
    if 0 < number <= len(movies):
        removed_movie = movies.pop(number - 1)
        write_movies_to_file(filepath, movies)
        print(f"Movie: {removed_movie} was deleted.")
    else:
        print("Invalid movie number.")

# Function to write the movies list back to the file
def write_movies_to_file(filepath, movies):
    with open(filepath, 'w') as file:
        for movie in movies:
            file.write(movie + '\n')

# Main part of the program
def main():
    filepath = 'movies.txt'  # Set the path to your movies file
    movies = get_movies_from_file(filepath)
    display_menu()
    while True:  # Loop to process user commands
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
