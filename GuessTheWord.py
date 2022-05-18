from os import system as _SystemCommands


def getResultFileAsList(_ResultFile):
    returnList = []
    for index, line in enumerate(_ResultFile):
        if index == 0:
            continue
        entry = line.strip().split(",  ")
        returnList.append(entry[2])
    return returnList


def guessThisWord(guessWord):
    try:
        print("Previous guesses: ")
        for entry in DeclinedWords:
            print(entry + "\n")
        print("Try: " + guessWord)
    except: 
        print("Error in Script.") 
        exit()

def findFittingWord(RL, GL, YL): #ResultList, GreenList, YellowList
    fittingWord = True
    while fittingWord == True:
    # Find Words fitting green
        for word in RL:
            fittingWord = True
            if word in DeclinedWords:
                continue

            # Find words not containing Black, the continue
            for x in word:
                if x in BlackLetters:
                    fittingWord = False
                    break
            if fittingWord == False:
                continue

            # Check if the word fits the Green Letters
            if len(GL) > 0:
                GreenSuccess = False
                for index, x in enumerate(word):
                    for listGreen in GL:
                        if not x in listGreen[0]:
                            continue
                        currentGreenLettersIndex = listGreen[1]
                        if not index in currentGreenLettersIndex:
                            continue
                        GreenSuccess = True
                if GreenSuccess == False:
                    continue

            # Check if Yellow Letters match:
            if len(YL) > 0:
                matches = 0
                for index, x in enumerate(word):
                    for listYellow in YL:
                        if not x in listYellow[0]:
                            continue
                        currentYellowLettersIndex = listYellow[1]
                        if index in currentYellowLettersIndex:
                            continue
                        matches +=1
                if matches == len(YL):
                    pass
                else: continue
            return word

def in_nested_list(my_list, item):
    """
    Determines if an item is in my_list, even if nested in a lower-level list.
    """
    if my_list == []:
        return False
    if item in my_list:
        return True
    else:
        return any(in_nested_list(sublist, item) for sublist in my_list if isinstance(sublist, list))


def setupLettersToList(Type, LL, CW): #Type(String), LetterList, CurrentWord
    returningLL = []

    # Check if LL is empty
    if LL == "":
        return returningLL
    
    #Create list
    for letterLL in list(LL):
        for index, letterCW in enumerate(CW):
            if letterLL in letterCW:
                if in_nested_list(returningLL, [letterLL, [index]]):
                    continue
                returningLL.append([letterLL, [index]])
    return returningLL

with open("Result.txt") as ResultFile:
    ResultList = getResultFileAsList(ResultFile) 

    global DeclinedWords
    DeclinedWords = []
    global BlackLetters
    BlackLetters = []


    GreenLetters = []
    YellowLetters= []
    CorrectGuess = False
    FirstGuess   = True
    CurrentWord  = None
    while CorrectGuess == False:
        _SystemCommands("CLS")
        print("If the answer was correct, just exit the script :)")
        CurrentWord = findFittingWord(ResultList, GreenLetters, list(YellowLetters))
        guessThisWord(CurrentWord)

        GreenLetters = input("If there are several greens, write then as many times! \nWrite All Green Letters: ")
        GreenLetters = setupLettersToList("Green", GreenLetters, CurrentWord)
        
        
        # YellowLetters = list(input("Write All Yellow Letters?: "))
        YellowLetters = input("Write All Yellow Letters?: ")
        YellowLetters = setupLettersToList("Yellow", YellowLetters, CurrentWord)
        #BUG The lists renew everytime, so the script does not remember previous Yellow attempts.
        # Remove Green letters from YellowList
        for entry in YellowLetters:
            if entry in GreenLetters:
                YellowLetters.remove(entry)

        BlackLetterThisTurn = []
        for letters in CurrentWord:
            if not in_nested_list(GreenLetters, letters):
                if not in_nested_list(YellowLetters, letters):
            # if letters not in GreenLetters or letters not in YellowLetters:
                    BlackLetterThisTurn.append(letters)
                    BlackLetters.append(letters)
        print("Black letters: " + "".join(map(str, BlackLetterThisTurn)))
        

        # BlackLetters = ["c","r","a"]
        # GreenLetter example: 
        # GreenLetters = [["e", [4]],["n", [1, 2, 3]]]


        DeclinedWords.append(CurrentWord) #Adds Current word to a list of declined words.