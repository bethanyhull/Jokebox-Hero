#
# Author: Bethany Hull
# Date:  April, 22, 2019
# Description: Jukebox Hero Project

#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
songList = []

#lists for the analize function
artists = []
albums = []
songs = []
totalTime = []


#
# Parameter
#   inputfile - A String with the name of a text file to convert to a Lit
#
# Return
#   A List containing each line from the text file
def getListFromFile (inputFile):
    outputList = []
    try:
        source = open(inputFile,"r")
        outputList =  source.readlines()
        source.close()
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    return outputList



#
# Component Four - Implement printCatalogStats() function here
#
def printCatalogStats(song):
    songArray = song.split(",")
    artists.append(songArray[0])
    albums.append(songArray[1])
    songs.append(songArray[2])
    totalTime.append(int(songArray[3]))


#
# Component Three - Implement findSongs() function here
#
def findSongs(songQuery):
    for i in songList:
        if songQuery in i.lower():
            printSong(i)


#
# Component Two - Implement printSong() function here
#
def printSong(song):
    songArray = song.split(",")
    time = int(songArray[3])
    seconds = time % 60
    minutes = int((time - seconds)/60)
    print("-------------------------------------\nArtist: " + songArray[0] + "\nAlbum: " + songArray[1] + "\nTitle: " + songArray[2] + "\nDuration: " + str(minutes) + ":" + str(seconds))

#
# Component One - Implement the printMenu() function here
##Write a custom function named printMenu() that displays the menu when the user enters “m”
def printMenu():
    print("(L)oad catalog")
    print("(S)earch catalog")
    print("(A)nalyse catalog")
    print("(P)rint catalog")
    print("(Q)uit")




#
# Component One - Main program loop begins here
#

##Implement Selection Menu Loop
##Use a while loop to continue running the program until the user enters “q”
while True:
##Implement (M)enu Option
    while True:
        print("Please enter a command (press m for Menu):")
        userInput = input().lower()
        if userInput == "m" or userInput == "l" or userInput == "s" or userInput == "a" or userInput == "p" or userInput == "q":
            break
        else:
            print("Oops! Wrong letter! Try again.")
    if userInput == "m":
        printMenu()

    elif userInput == "l":
        print("Please enter a file name ending in .csv:")
        fileName = input()
        songList = getListFromFile(fileName)

    elif userInput == "s":
        print("Please enter the word or terms you're searching for:")
        userSearch = input()
        findSongs(userSearch)


    elif userInput == "a":
        for i in songList:
            printCatalogStats(i)

        artists = list(dict.fromkeys(artists))
        print("Artists: "+ str(len(artists)))

        albums = list(dict.fromkeys(albums))
        print("Albums: "+ str(len(albums)))

        songs = list(dict.fromkeys(songs))
        print("Songs: "+ str(len(songs)))

        sumOfTime = sum(totalTime)
        print("Time in Seconds: "+ str(sumOfTime))


    elif userInput == "p":
        for i in songList:
            printSong(i)

    elif userInput == "q":
        break

##Implement (Q)uit Option
##Exit the selection menu loop when the user enters “q”
##Stub out the (L)oad, (S)earch, (A)nalyse and (P)rint options and print a message saying that functionality has not been implemented yet if the user selects those options.
##If the user enters an invalid command, display the input prompt again

















#
# Component One - Program ends here
#
print("Leaving Jukebox Hero...  Goodbye!")
