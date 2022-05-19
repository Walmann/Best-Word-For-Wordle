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
        if len(DeclinedWords) >= 1:
            print("Previous guesses: ")
            for entry in DeclinedWords:
                print(entry)
        print('\n\033[1;30;43m Try this: ' + guessWord + ' \033[0;0m')
    except:
        print("Error in Script.")
        exit()


def findFittingWord(RL):  # ResultList
    fittingWord = True
    while fittingWord == True:
        # Find Words fitting green
        for word in RL:
            fittingWord = True
            if word in DeclinedWords:
                continue

            # Find words not containing Black, then continue
            for x in word:
                if x in BlackLetters:
                    fittingWord = False
                    break
            if fittingWord == False:
                continue

            # Check if the word fits the Green Letters
            if len(GreenLetters) > 0:
                matchesGL = 0
                for index, x in enumerate(word):
                    for listGreen in GreenLetters:
                        if x in listGreen[0]:
                            if index in listGreen[1]:
                                matchesGL += 1
                        continue

                if matchesGL == len(GreenLetters):
                    pass
                else:
                    continue

            # Create list of indexes Yellow shall ignore. No need to check a space that is supposed to be green
            indexesToIgnoreForYellow = []
            for xIndex in GreenLetters:
                for xxIndex in xIndex[1]:
                    indexesToIgnoreForYellow.append(xxIndex)

            # Check if Yellow Letters match:
            if len(YellowLetters) > 0:
                matchesYL = 0

                for YLEntry in YellowLetters:
                    for wordIndex, wordLetter in enumerate(word):
                        if wordLetter in YLEntry[0]:
                            if not wordIndex in YLEntry[1]:
                                matchesYL += 1

                if matchesYL == len(YellowLetters):
                    pass
                else:
                    continue
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


# Type(String), LetterList, CurrentList, CurrentWord
def setupLettersToList(Type, LL, CL, CW):
    returningLL = CL

    # Check if LL is empty
    if LL == "":
        return returningLL

    # Create list
    for letterLL in list(LL):
        for index, letterCW in enumerate(CW):
            if letterLL in letterCW:
                if in_nested_list(returningLL, [letterLL, [index]]):
                    if Type == "Yellow":
                        returningLL.append([letterLL, [index]])
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
    YellowLetters = []
    CorrectGuess = False
    FirstGuess = True
    CurrentWord = None
    while CorrectGuess == False:
        _SystemCommands("CLS")
        print("If the answer was correct, just exit the script :)")
        CurrentWord = findFittingWord(ResultList)
        guessThisWord(CurrentWord)

        GreenLettersInput = input(
            "If there are several greens, write then as many times! \nWrite All Green Letters: ")
        GreenLetters = setupLettersToList(
            "Green", GreenLettersInput, GreenLetters, CurrentWord)

        YellowLettersInput = input("Write All Yellow Letters?: ")
        YellowLetters = setupLettersToList(
            "Yellow", YellowLettersInput, YellowLetters, CurrentWord)

        # Remove entries in YellowLetters, if an entry in GreenLetters exist in that index.
        for YLIndex, YLEntry in enumerate(YellowLetters):
            for GLEntry in GreenLetters:
                if GLEntry in YLEntry:
                    YellowLetters.remove(GLEntry)
                if YLEntry[1] == GLEntry[1]:
                    YellowLetters.pop(YLIndex)

        BlackLetterThisTurn = []
        for letters in CurrentWord:
            if not in_nested_list(GreenLetters, letters):
                if not in_nested_list(YellowLetters, letters):
                    # if letters not in GreenLetters or letters not in YellowLetters:
                    BlackLetterThisTurn.append(letters)
                    BlackLetters.append(letters)
        print("Black letters: " + "".join(map(str, BlackLetterThisTurn)))

        # GreenLetter example:
        # GreenLetters = [["e", [4]],["n", [1, 2, 3]]]

        # Adds Current word to a list of declined words.
        DeclinedWords.append(CurrentWord)
