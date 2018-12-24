#!/usr/bin/env python3
import list as list
import add as add
import delete as delete
import find as find


def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by year")
    print("exit - Exit program")
    print()    

                  
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 12.95],
                  ["On the Waterfront", 1954, 9.95], 
                  ["Cat on a Hot Tin Roof", 1958, 7.95],
                  ["Long Hot Summer", 1958, 9.95]]
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list.list(movie_list)
        elif command == "add":
            add.add(movie_list)
        elif command == "del":
            delete.delete(movie_list)
        elif command == "find":
            find.find_by_year(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
