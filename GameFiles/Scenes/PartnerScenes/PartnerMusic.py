from time import sleep
from ...Input import yesorno

# plays immediately and doesnt take time if on dance floor and music is terrible and it hasnt played yet


def partnermusiccontent(player):
    print("Your partner gives you this look")
    sleep(2)
    print("mouthing something like ")
    sleep(2)
    print("")
    print("     This music is terrible")
    print("")
    sleep(2)
    print("you feel your willpower draining")
    print("this is totally killing your vibe")
    print("")
    sleep(3)
    print("     Let's go smoke")
    print("     Better to avoid the dance floor when the music's this bad.")
    print("")

    print("      Do you wanna go smoke? (y/n) ", end="")
    option = yesorno()

    if option == True:
        print("You both make your way to the smoking room.")
        sleep(2)
        print("Your partner looks half amused as they tell you")
        print("")
        sleep(1)
        print("     That was nonsensical")
        sleep(2)
        print("")
        print("you consider making some time until the bad music blows over.")
        player.location = player.rooms["smoking room"]
        player.NPCs["partner"].location = player.rooms["smoking room"]

    elif option == False:
        print("You decide to stay here for the moment.")
        print("You can feel the fun slowly draining out of your body.")
        player.modify_stat("lit", 10, False)
    print("")
    return True
