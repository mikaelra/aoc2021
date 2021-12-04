# Imports
from numpy import zeros, array, array_equal
import random


printTests = True
# Read in file
n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(line)

# First line is order of Bingo Numbers
bingoNumbers = n[0].split(',')
bingoNumbers = [int(i) for i in bingoNumbers]
print("These are the winning bingo number:")
print(bingoNumbers)
print('\n')

# Create function which checks which number of an 5x5 bing-array is played
def getPlayedMatrixOfBoard(board, playedNumbers, printout=False):
    IsPlayedArray = zeros((5,5))
    for i in range(5):
        for j in range(5):
            if board[i][j] in playedNumbers:
                IsPlayedArray[i][j] = 1
    if printout:
        for i in range(5):
            print (IsPlayedArray[i])
    
    # Returns 5x5 array with 1's where numbers are played and
    # 0's where not
    return IsPlayedArray

# Return array of 0's and 1's where 1's are 
def hasCheckedArrayWon(checkedArray):
    for i in range(5):
        # Check horizontal lines if there is 1's all across the line
        hasWon = True
        for j in range(5):
            if checkedArray[i][j] == 0:
                hasWon = False
        if hasWon:
            return True
        # Check vertical lines    
        hasWon = True
        for j in range(5):
            if checkedArray[j][i] == 0:
                hasWon = False
        if hasWon:
            return True
    
    return False

# Combines the two functions above
# Finds out if board has won
def checkIfBoardHasWon(board, playedNumbers, printout=False):
    playedMatrix = getPlayedMatrixOfBoard(board, playedNumbers)
    hasBoardWon = hasCheckedArrayWon(playedMatrix)
    if hasBoardWon and printout:
        print("This board has won:")
        for i in range(5):
            print(board[i])
        print("These are the played numbers:")
        print(playedNumbers)
    elif not hasBoardWon and printout:
        print("This board has NOT won:")
        for i in range(5):
            print(board[i])
        print("These are the played numbers:")
        print(playedNumbers)
    
    # Returns true if board has won with the played numbers
    return hasBoardWon


# Tests
if printTests:
    print("Some tests of checking of boards:")
    a = zeros((5,5))
    b = a.copy()
    c = a.copy()
    d = a.copy()
    for i in range(5):
        a[0][i] = 4
        b[i][3] = 5
        c[1][i] = random.choice([17,24])

    checkIfBoardHasWon(a, [4], printout=True)
    checkIfBoardHasWon(b, [5], printout=True)
    checkIfBoardHasWon(c, [17, 24], printout=True)
    checkIfBoardHasWon(d, [39], printout=True)
    print('\n')

# Read in the bingo-boards to a list of 5x5 arrays
def getBingoBoardsFromFile(printout=False):
    index = 0
    bingoBoards = []
    tempBingoBoard = zeros((5,5))
    for i in range(2, len(n)):
        if len(n[i]) < 4:
            index = 0
        else:
            tempLine = n[i]
            firn = int(n[i][0:2])
            secn = int(n[i][3:5])
            thin = int(n[i][6:8])
            foun = int(n[i][9:11])
            fivn = int(n[i][12:14])
            tempBingoBoard[index][0] = firn
            tempBingoBoard[index][1] = secn
            tempBingoBoard[index][2] = thin
            tempBingoBoard[index][3] = foun
            tempBingoBoard[index][4] = fivn

            index+=1
            if index == 5:
                bingoBoards.append(tempBingoBoard)
                tempBingoBoard = zeros((5,5))

    
    if printout:
        if len(bingoBoards) > 0:
            print("Succesfully read in " + str(len(bingoBoards)) + " bingoboards!")
        else:
            print("Could not read in any bingoboards!")

    return bingoBoards
    
bingoBoards = getBingoBoardsFromFile(printout=False)


def getWinningBoard(bingoboards, playednumbers, printout=False):
    for i in range(len(playednumbers)):
        currNumbers = playednumbers[0:i]
        for board in bingoboards:
            if checkIfBoardHasWon(board, currNumbers):
                if printout:
                    checkIfBoardHasWon(board, currNumbers, printout=True)
                    print("This is where the numbers are hit:")
                    getPlayedMatrixOfBoard(board, currNumbers, printout=True)
                return board, currNumbers[-1], getPlayedMatrixOfBoard(board, currNumbers)
    return 0

winningBoard, lastNumber, markedNumbers = getWinningBoard(bingoBoards, bingoNumbers, printout=True)

def calculateScore(board, lastNumber, markedNumbers):
    sumOfUnmarkeNumbers = 0
    for i in range(5):
        for j in range(5):
            if markedNumbers[i][j] ==0:
                sumOfUnmarkeNumbers += board[i][j]

    print("Sum of unmarked numbers of winning board is:")
    print(sumOfUnmarkeNumbers)
    print("The final score is the sum * the last number:")
    print (str(sumOfUnmarkeNumbers) + " * " + str(lastNumber) + " = " + str(sumOfUnmarkeNumbers*lastNumber))

calculateScore(winningBoard, lastNumber, markedNumbers)

######### Task 2 ################

def getLastWinningBoard(bingoboards, playednumbers, printout=False):
    wonBoards = []
    for i in range(len(playednumbers)):
        currNumbers = playednumbers[0:i]
        for board in bingoboards:
            if checkIfBoardHasWon(board, currNumbers):
                isAdded = False
                for j in range(len(wonBoards)):
                    if array_equal(board, wonBoards[j]):
                        isAdded = True
                if not isAdded:
                    wonBoards.append(board)
        if len(wonBoards) == 100:
            if printout:
                checkIfBoardHasWon(wonBoards[-1], currNumbers, printout=True)
                print("This is where the numbers are hit:")
                getPlayedMatrixOfBoard(wonBoards[-1], currNumbers, printout=True)
            return wonBoards[-1], currNumbers[-1], getPlayedMatrixOfBoard(wonBoards[-1], currNumbers)
    return 0
        

lastWinningBoard, lastNumber, markedNumbers = getLastWinningBoard(bingoBoards, bingoNumbers, True)

calculateScore(lastWinningBoard, lastNumber, markedNumbers)