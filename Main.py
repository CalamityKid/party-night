from GameFiles.GameLoop import gameloop
from GameFiles.Input import yesorno

another_loop = True
while another_loop == True:
    gameloop()
    print("")
    print(" Would you like to try again? (y/n) ", end="")
    print("but it doesnt work")
    option = yesorno()
    if option == False:
        another_loop = False


input()
input()
