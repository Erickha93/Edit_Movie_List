def find_by_year(movie_list):
    year = int(input("Year: "))    
    for movie in movie_list:
        if movie[1] == year:
            print(movie[0] + " was released in " + str(year))
    print()
