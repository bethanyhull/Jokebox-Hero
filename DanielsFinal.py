#----------------------------------------------------------------------------------------------------
#Function that opens the inputted source file to read the lines of the CSV file
#Includes a try/catch to catch errors and print an error statement
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#Open array lists and boolean values declared for later global use
#----------------------------------------------------------------------------------------------------
outputList = []
fin = []
aList = []
albumList = []
titleList = []
durationList = 0
loadedFile = False
error = "Please select a file to load first. \n"
Dur = 0
#----------------------------------------------------------------------------------------------------


def printSong(song):
    songParameter = song.split(",")
    Dur = 0
    Artist = songParameter[0]
    Album = songParameter[1]
    Title = songParameter[2]
    Duration = songParameter[3]
    
    Dur += (int(Duration))
    output = ("Artist = " + Artist + "\n")
    output += ("Album = " + Album + "\n")
    output += ("Title = " + Title + "\n")
    print(output, end="")

    days = (int(Dur/86400))
    hours = (int(Dur/3600))
    minutes = (int(Dur/60%60))
    seconds = (int(Dur%60))

    if days > 0 and hours > 0:
        print ("Duration = ", end = "")
        print("{:02d}:{:02d}:{:02d}:{:02d}\n".format(days,hours,minutes,seconds))
    elif days <= 0 and hours > 0:
        print ("Duration = ", end = "")
        print("{:02d}:{:02d}:{:02d}\n".format(hours,minutes,seconds))
    elif days <= 0 and hours <= 0:
        print ("Duration = ", end = "")
        print("{:02d}:{:02d}\n".format(minutes,seconds))   
            

    
    

def analyzeCatalog(outputList):
    global durationList
    if loadedFile == False:
        print(error)
        selectionMenu()
    elif loadedFile == True:  
        songParameter = outputList.split(",")

        Artist = songParameter[0]
        Album = songParameter[1]
        Title = songParameter[2]
        Duration = songParameter[3]

        aList.append(Artist)
        albumList.append(Album)
        titleList.append(Title)
        durationList += int(Duration)


#----------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------
def runIt(outputList):
    global durationList
    if loadedFile == False:
        print(error)
        selectionMenu()
    elif loadedFile == True:        
        for x in outputList:
            analyzeCatalog(x)
        l1 = (set(aList))
        l2 = (set(albumList))
        l3 = (set(titleList))

        days = (int(durationList/86400))
        hours = (int(durationList/3600))
        minutes = (int(durationList/60%60))
        seconds = (int(durationList%60))

        print ("Number of Artist: ", end = "")
        print (len(l1))
        print ("Number of Albums: ", end = "")
        print (len(l2))
        print ("Number of Titles: ", end = "")
        print (len(l3))

        if days > 0 and hours > 0:
            print ("Length of Album: ", end = "")
            print("{:02d}:{:02d}:{:02d}:{:02d}\n".format(days,hours,minutes,seconds))
        elif days <= 0 and hours > 0:
            print ("Length of Album: ", end = "")
            print("{:02d}:{:02d}:{:02d}\n".format(hours,minutes,seconds))
        elif days <= 0 and hours <= 0:
            print ("Length of Album: ", end = "")
            print("{:02d}:{:02d}\n".format(minutes,seconds))
        durationList = 0
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
#Function that opens the inputted source file to read the lines of the CSV file
#Includes a try/catch to catch errors and print an error statement
#----------------------------------------------------------------------------------------------------
def getListFromFile(file):
        global loadedFile
        jList = []
        try:
                source = open(file,"r")
                jList =  source.readlines()
                source.close()
                print("\nFile: '" + file + "' successfully loaded.\n")
                loadedFile = True
        except FileNotFoundError:
                print("Unable to open input file: '" + file + "'\n")
        return jList
#----------------------------------------------------------------------------------------------------        

#----------------------------------------------------------------------------------------------------
#Function used to loop through the printSong() function to get an overall print of the csv file
#if/elif loop is used with a boolean value so that if a csv file isn't loaded, it will return
#an error message and send you back to the selection menu.
#----------------------------------------------------------------------------------------------------
def printSongList(outputList):
    if loadedFile == False:
        print(error)
        selectionMenu()
    elif loadedFile == True:
        for x in outputList:
            printSong(x)
            print("\n")
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#Function to take user input, compare it to all the strings in the file, and return all search
# results.
#if/elif boolean statement to make sure the function won't run without a loaded csv file
#The for loop cycles through the appended array of search results and prints the results
#Because I'm storing the results in an array, I'm using the .clear() function to clear the array
# so that it doesn't repeatedly store results in said array.
#----------------------------------------------------------------------------------------------------
def searchCatalog(queryString, outputList):
        y = "yes"
        n = "no"
        save = True
        if loadedFile == False:
            print(error)
            selectionMenu()
        elif loadedFile == True:
            global fin
            for x in outputList:
                if queryString.lower() in x.lower():
                    fin.append(x)
            print ("-----------------------------------------------")
            print ("Number of results: " + str(len(fin)) + ".")
            print ("-----------------------------------------------")
        
            for x in fin:
                printSong(x)
                print("\n")
            while save == True:
                fileSave = input("Would you like to save? Please enter 'yes' or 'no'. ")
                if fileSave.lower() == y.lower():
                    newFileName = input("What would you like to name the file? ")
                    savedFile = open(newFileName + ".csv", "w")
                    print("\nFile successfully saved as: '" + newFileName + ".csv'\n")
                    i = 0
                    for x in fin:
                        savedFile.writelines(fin[i])
                        i += 1
                    savedFile.close()    
                    save = False
                elif fileSave.lower() == n.lower():
                    save = False
                elif fileSave.lower() != y.lower() or n.lower():
                    print("Please enter 'yes' or 'no'.")            
            fin.clear()
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#Main function that launches the selectionMenu(), always True, takes users input to display the menu
#----------------------------------------------------------------------------------------------------
def selectionMenu():
    while True:
        choice = input("Please enter a command (press 'm' for Menu): ")
        if choice.lower() == ("m"):
            printMenu()
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#printMenu() function shows all available choices for what you can do with the csv file.
#Basic if/elif layout for menu choices
#outputList decladed global (which is the empty array the csv file will be sent to)
 #so that it may be referenced
#----------------------------------------------------------------------------------------------------            
def printMenu():
    global outputList
    menu = input("\n(L)oad catalog \n(S)earch catalog \n(A)nalyze catalog \n(P)rint catalog \n(Q)uit\n" + "\n")
    if menu.lower() == ("l"):
        file = input("What file would you like to use? ")
        outputList = getListFromFile(file)
    elif menu.lower() == ("s"):
        queryString = input("What keyword would you like to search for? ")
        searchCatalog(queryString, outputList)
    elif menu.lower() == ("a"):
         runIt(outputList)
    elif menu.lower() == ("p"):
         printSongList(outputList)
    elif menu.lower() == ("q"):
         exit()
    else:
         print("Please enter a valid choice")
         printMenu()
#-----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#The only actual function called that gets the whole thing running!
#----------------------------------------------------------------------------------------------------
selectionMenu()
#----------------------------------------------------------------------------------------------------
