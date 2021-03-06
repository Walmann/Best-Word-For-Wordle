

letterDict = {
    0: {
    },
    1: {
    },
    2: {
    },
    3: {
    },
    4: {
    },
}
# letterDict = {}


def createTopLetter(letterDict):
    letterscore = []
    # newLetterscore = []
    newLetterscore = {}


    for keys in letterDict:
            letterscore.append([letterDict[keys], str(keys)])
    newList = sorted(letterscore)
    for index, element in enumerate(newList):
        newLetterscore[element[1]] = index
        # newLetterscore.append([str(element[1]), index])

    return newLetterscore


def striken(text):
    return ''.join(chr(822)+t for t in text)
    

with open("WordLists/wordlistNYTimes.txt", "r") as wordlistFile:

    wordList = []
    for item in wordlistFile:
        wordList.append(item.strip())


    for lines in wordList:
        for index, letter in enumerate(lines):
            if not letter.strip() == "":
                letter = letter.strip()
                try:
                    letterDict[index][letter] += 1
                except KeyError:
                    try:
                        letterDict[index][letter] = 1
                    except KeyError:
                        letterDict[index] = index
                        letterDict[index][letter] = 1

    listLetterOne = createTopLetter(letterDict[0])
    listLetterTwo = createTopLetter(letterDict[1])
    listLetterThree = createTopLetter(letterDict[2])
    listLetterFour = createTopLetter(letterDict[3])
    listLetterFive = createTopLetter(letterDict[4])
    

    wordHighScore = []
    for lineEntry in wordList:
        lineEntry = lineEntry.strip()
        wordScore = 0
        wordScoreArray = []
        currentWordContainsLetters = []
        for index, letter in enumerate(lineEntry):
            if index == 0:
                currentList = listLetterOne
            if index == 1:
                currentList = listLetterTwo
            if index == 2:
                currentList = listLetterThree
            if index == 3:
                currentList = listLetterFour
            if index == 5:
                currentList = listLetterFive



            if letter in currentWordContainsLetters:
                wordScoreArray.append(striken(str(letterScore))) # Create strikethrough to number that does not count towards the total score
                continue
            
            currentWordContainsLetters.append(letter)

            letterScore = int(str(currentList[letter]))

            wordScoreArray.append(letterScore)

            wordScore = wordScore + letterScore

        wordHighScore.append([str(wordScore).zfill(3), lineEntry, wordScoreArray])

    with open("Result.txt", "w+", encoding="UTF-8") as Results:
        sortetHighScore = sorted(wordHighScore, key=lambda x: x[0], reverse=True)
        Results.write('Position, Score, Word, FirstLetterScore, SecondLetterScore, ThirdLetterScore, FourthLetterScore, FifthLetterScore\n') # Create CSV header
        for index, line in enumerate(sortetHighScore):
            Results.write(str(index +1).zfill(5) + ",  " + str(line[0]) + ",  " + str(line[1]) +",  "+ str(line[2]) + "\n")
