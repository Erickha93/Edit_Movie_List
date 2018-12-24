def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 0
        for movie in movie_list:
            row = movie
            print(str(i+1) + ". " + row[0] + " (" + str(row[1]) + ")" + " $" + str(row[2]))
            i += 1
        print()
