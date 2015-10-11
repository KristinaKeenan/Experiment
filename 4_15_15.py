def findInformation(movieName,movieDictionary):
    if movieName in movieDictionary:
        return movieDictionary[movieName]
    

def addMovie(movie,year,genre,director,movieDictionary):
    movieDictionary[movie] = [year,genre,director]
    return movieDictionary
    



def main():

    movieDictionary = {'High School Musical':['2006','Musical','Kenny Ortega']}
    
    movieOrEntry = input("Do you want to 'add' or 'find' a movie?")
    if movieOrEntry == "find":
        movieName = input('Enter a movie:')
        theInformation = findInformation(movieName,movieDictionary)
        print(movieName)
        for i in theInformation:
            print(i)
        goAgain = input("Do you want to restart the program? Type in 'yes' or 'no'.")
        if goAgain == "yes":
            main()
        else:
            print("Thanks for using the program!")
    elif movieOrEntry == "add":
        movieToAdd = input('Enter a movie title:')
        yearToAdd = input('Enter its year:')
        genreToAdd = input('Enter its genre:')
        directorToAdd = input('Enter its director:')
        addMovie(movieToAdd,yearToAdd,genreToAdd,directorToAdd,movieDictionary)
        goAgain = input("Do you want to restart the program? Type in 'yes' or 'no'.")
        if goAgain == "yes":
            main()
        else:
            print("Thanks for using the program!")
    else:
        print("Thanks for using the program!")
    


main()
