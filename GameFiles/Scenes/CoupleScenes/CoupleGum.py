from time import sleep
from ...Scripts.Blocks import items
from ...Input import yesorno


def coupleGumcontent(player):
    print("Your friends come to you.")
    sleep(1)
    print("")
    print("     Baby, you got a bad case of cottonmouth.")
    sleep(1)
    if items["chewing gum"] not in player.items:
        print("     We've got your back.")
        sleep(2)
        print("one of them says while the other one hands you some chewing gum.")
        print("")
        print("     Do you want some chewing gum? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You accept the gum and put it in your pocket.")
            player.items.append(items["chewing gum"])
        elif option == False:
            print("You say no, thank you.")
            sleep(2)
            print("")
            print("     It'll be good, here you go, think about it.")
            sleep(2)
            print("they put some chewing gum in your pocket nonetheless.")
        player.items.append(items["chewing gum"])
        return None
    elif items["chewing gum"] in player.items:
        print("     Babe, maybe it's time to use that chewing gum.")
        sleep(2)
        print("one of them says while the other looks around.")
        return None
