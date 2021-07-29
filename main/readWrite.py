def fileToString(filename):

    with open (filename, "r") as userInput:
        userFile=userInput.readlines()

    userString = ""

    for line in userFile:
        userString = userString + line
    
    return userString

def stringToFile(filename, message):
    
    outputFile = open(filename, "a")
    outputFile.write(message)
    outputFile.close()

