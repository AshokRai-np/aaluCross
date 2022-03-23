table = [[0 for i in range(3)] for j in range(3)]
status = 0
sign = 'Y'
def draw():
    for i in range(3):
        for j in range(3):
            print(table[i][j], end=" ")
            print("|", end=" ")
        print("\n------------")

def takePosition():
    row = int(input("Enter the row"))
    col = int(input("Enter the col"))
    return row, col

def setPosition(row, col, sign):
    if table[row][col] == 0:
        table[row][col] = sign
    else:
        print("The position is taken. Take next row and col")
        row, col = takePosition()

def gameStatus(sign):
    if (table[0][0] == sign and table[0][1] == sign and table[0][2] == sign) or\
            (table[1][0] == sign and table[1][1] == sign and table[1][2] == sign) or\
            (table[2][0] == sign and table[2][1] == sign and table[2][2] == sign) or\
            (table[0][0] == sign and table[1][0] == sign and table[2][0] == sign) or\
            (table[0][1] == sign and table[1][1] == sign and table[2][1] == sign) or\
            (table[0][2] == sign and table[1][2] == sign and table[2][2] == sign):
            return 1
    elif(table[0][0] == sign and table[1][1] == sign and table[2][2] == sign) or \
            (table[0][2] == sign and table[1][1] == sign and table[2][0] == sign):
        return 1
    elif (table[0][0] != 0 and table[0][1] != 0 and table[0][2] != 0 and
          table[1][0] != 0 and table[1][1] != 0 and table[1][2] != 0 and
          table[2][0] != 0 and table[2][1] != 0 and table[2][2] != 0):
        return -1
    else:
        return 0

draw()
while status == 0:

    row, col = takePosition()
    setPosition(row, col, sign)
    status = gameStatus(sign)
    draw()

    if status == 1:
        print("*** " + sign + " won the game ***")
    if status == -1:
        print("It is a draw")
        status = 1

    if sign == 'Y':
        sign = 'X'
    else:
        sign = 'Y'


