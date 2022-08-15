# Title : Suduko solver using backtracking
# Author : Javier Seidel

# input any suduko puzzle you wish to be solved. Blanks are represented by 'X'. Puzzle must be solvable. Puzzle must be 9'X'9
sudukoPuzzle = [
    ['X','X','X',8,'X','X',9,'X','X'],
    ['X',9,'X','X',7,'X','X','X',4],
    ['X',8,4,'X','X','X','X',6,'X'],
    ['X','X','X',4,1,'X',2,'X','X'],
    ['X','X',3,'X','X','X',5,'X','X'],
    ['X','X',1,'X',6,9,'X','X','X'],
    ['X',2,'X','X','X','X',7,4,'X'],
    [9,'X','X','X',2,'X','X',3,'X'],
    ['X','X',7,'X','X',6,'X','X','X']
]

# prints the puzzle to the console
def printPuzzle(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end ="")

# finds any blank spaces, which are represented by 0's
def findBlank(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 'X':
                return (i ,j)
    return False

# checks to see if the move is valid. makes sure it does not break the rules of suduko
def isMoveValid(puzzle, choice, position):
    # row
    for i in range(9):
        if puzzle[position[0]][i] == choice and position[1] != i:
            return False
    # col
    for i in range(9):
        if puzzle[i][position[1]] == choice and position[0] != i:
            return False
    # section
    x = int(position[1] / 3) 
    y = int(position[0] / 3) 

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if puzzle[i][j] == choice and (i, j) != position:
                return False

    return True     

# this is our solver algorithm. recursivley checks every blank space, and makes sure the move is valid
def solver(puzzle):
    found = findBlank(puzzle)
    if found == False:
        return True
    else:
        row, col = found

    for i in range(1, 10):
        if isMoveValid(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if solver(puzzle):
                return True
            
            puzzle[row][col] = 'X'

    return False

# here is where the puzzle is printed to the screen, and then solved and then the solution that is found is printed
def printSol():
    print("\n- - - - - - - - - - - - - - - - - -\n")
    print("Welcome to the suduko solver. Below is your puzzle printed to the console")
    print("\n- - - - - - - - - - - - - - - - - -\n")
    printPuzzle(sudukoPuzzle)
    print("\n- - - - - - - - - - - - - - - - - -\n")
    print("Here is your finished puzzle which has been solved using backtracking")
    print("\n- - - - - - - - - - - - - - - - - -\n")
    solver(sudukoPuzzle)
    printPuzzle(sudukoPuzzle)


printSol()