#Caleb Callaway
#4/27/18
#matrixDemo.py - Listception

def printBoard(board):
    for row in range(0,3):
        for col in range (0,3):
            print (board[row][col],end = " ")
        print()


board = [["a","b","c"],["d","e","f"],["g","h","i"]]

printBoard(board)

r = int(input("Enter a row: "))
c = int(input("Enter a column: "))