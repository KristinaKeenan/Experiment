def getOrd(letters):
 

    for aChar in letters:
        print(aChar, "=",ord(aChar))

    for aChar in letters.upper():
        print(aChar, "=",ord(aChar))


def main():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    getOrd(alphabet)


main()
