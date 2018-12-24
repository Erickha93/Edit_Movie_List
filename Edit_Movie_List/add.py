def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    price = input("Price: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")
