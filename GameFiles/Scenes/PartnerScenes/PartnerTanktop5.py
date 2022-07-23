from time import sleep
from ...Input import yesorno

# liga con tanktop, happens spontaneously if it hasnt run and tanktop flirt is higher 10.
def partnertanktop5content(player):
    print("looks like your partner's flirting is paying off")
    print("the cutie in the tanktop's bouncing that energy right back")
    sleep(2)
    print("your partner gives you a quick look to check if you're okay with it")
    sleep(2)
    print("without thinking about it you give a small nod")
    print("and they disappear together")
    sleep(2)
    print("     You stop for one second and check in with yourself.")
    inputstring = None
    while inputstring == None:
        print("     How do you feel about this?", end=" ")
        inputstring = input()
        print(
            "Do you really feel {inputstr}? (y/n) ".format(inputstr=inputstring), end=""
        )
        option = yesorno()
        if option == False:
            inputstring = None
        elif option == True:
            print("")
            print(("You do really feel {inputstr} then.").format(inputstr=inputstring))
            print("and that's that.")
            sleep(2)

            print("they show up after a few minutes")
            print(
                ("your partner looks at you and you feel even more {inputstr}.").format(
                    inputstr=inputstring
                )
            )
            print("you ask how it went")
            print("")
            sleep(2)
            print("It went well, it was fun.")
            print("You decide to talk more about it back home")
            print("and go back to partying.")
            player.memories.append("Partner Hookup")
            return True
