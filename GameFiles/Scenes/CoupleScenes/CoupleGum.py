from ...Scripts.Blocks import items
from ...Input import yesorno


def coupleGumcontent(player):
    print("Your friends come to you.")
    print("")
    print("     Baby, you got a bad case of cottonmouth.")
    if items["chewing gum"] not in player.items:
        print("     We've got your back.")
        print("one of them says while the other one hands you some chewing gum.")
        print("     Do you want some chewing gum? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You accept the gum and put it in your pocket.")
            player.items.append(items["chewing gum"])
        elif option == False:
            print("You say no, thank you.")
            print("     It'll be good, here you go, think about it.")
            print("they put some chewing gum in your pocket nonetheless.")
        player.items.append(items["chewing gum"])
        return None
    elif items["chewing gum"] in player.items:
        print("     Babe, maybe it's time to use that chewing gum.")
        print("one of them says while the other looks around.")
        return None
