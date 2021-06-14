# game of tic tac toe

def tic_tac_toe():
    print("********______TIC TAC TOE______*********")
    print("")
    grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # grid = ["Null", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def if_won(grid):
        if grid[1] == grid[2] == grid[3]:
            return 1
        elif grid[4] == grid[5] == grid[6]:
            return 1
        elif grid[7] == grid[8] == grid[9]:
            return 1
        elif grid[1] == grid[4] == grid[7]:
            return 1
        elif grid[2] == grid[5] == grid[8]:
            return 1
        elif grid[3] == grid[6] == grid[9]:
            return 1
        elif grid[1] == grid[5] == grid[9]:
            return 1
        elif grid[3] == grid[5] == grid[7]:
            return 1
        elif(grid.count("X")+grid.count("O") == 9):
            return 2
        else:
            return 0

    def print_grid(grid):
        print(grid[1].rjust(10) + " | " + grid[2] + " | " + grid[3])
        print("---+---+---".rjust(19))
        print(grid[4].rjust(10) + " | " + grid[5] + " | " + grid[6])
        # print("-+-+-".rjust(14))
        print("---+---+---".rjust(19))
        print(grid[7].rjust(10) + " | " + grid[8] + " | " + grid[9])

        print("")
    inp = input("Player 1, choose x or o :: ")
    print("")
    if(inp=="x"):
        x = "X"
        o = "O"
    else:
        o = "X"
        x = "O"


    while if_won(grid) == 0:
        print_grid(grid)
        num = input("Choose any element between 1 to 9:- ")
        if (grid[int(num)] == "X" or grid[int(num)] == "O"):
            print("!!!!!!!INVALID INPUT .... PLACE ALREADY ASSIGNED VALUE!!!!!!!")

        else:
            grid[int(num)] = x
            x, o = o, x

    if(if_won(grid) == 1):
        print_grid(grid)
        print("---------Player " + o + " wins.---------")

    elif(if_won(grid) == 2):
        print_grid(grid)
        print("---------Match Tied---------")
    print("-+-"*20)


tic_tac_toe()
while(True):
    reply = input("Do you want to play again!!.. Enter y(YES) or n(NO)_ ")
    if reply == "y":
        tic_tac_toe()
    elif reply == "n":
        break
input("Prees ENTER to exit..")
