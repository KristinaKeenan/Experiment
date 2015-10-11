def censor(phrase):

    """ This function changes any 4 letter word in the phrase to '@*$%' and prints the new phrase."""

    for i in range(len(phrase)):
        if len(phrase[i]) == 4:
            phrase[i] = "@*$%"
    censoredPhrase = ""
    for i in phrase:
        censoredPhrase = censoredPhrase + i + " "
    print("Your censored phrase:",censoredPhrase)


def main():

    """This is the main function, which takes in an input and feeds it to the censor function."""
    
    phrase = input("What phrase do you want to censor?")
    phrase = phrase.split(" ")
    censor(phrase)


main()
