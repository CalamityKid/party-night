from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks import items

# they offer chewing gum, give you borrow gum memory


def coupletimes1content(player):
    player.memories.append("Borrow Gum")
    print("")
    if player.location == player.rooms["smoking room"]:
        print(
            "     I wanna dance tonight babe, but the music is like, REALLY BAD right now."
        )
        sleep(2)
        print("one of them says while the other is talking to another friend.")
        sleep(2)
        print("")
        print("     I missed partying but I didn't miss this part.")
        sleep(1)
        print("You talk a bit about how the week went and stuff.")
        sleep(1)
        print("They offer you some chewing gum.")
        print("")
        print("     Do you want some chewing gum? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You take the chewing gum and put it in your pocket.")
            player.items.append(items["chewing gum"])
        elif option == False:
            print("You kindly turn down the offer.")
        player.NPCs["couple"].times_talked = 2
        return True

    elif player.location == player.rooms["bathroom"]:
        player.NPCs["smile"].location = player.location
        print(
            "     I hope the music's good tonight, I really wanna dance to some good shit."
        )
        sleep(2)
        print("one of them says while the other talks to the smile ambassador.")
        sleep(1)
        print("You comment how last time the music wasn't great.")
        print("")
        print("They offer you some chewing gum.")
        print("     Do you want some chewing gum? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You take the chewing gum and put it in your pocket.")
            player.items.append(items["chewing gum"])
        elif option == False:
            print("You kindly turn down the offer.")
        player.NPCs["couple"].times_talked = 2
        return True

    elif player.location == player.rooms["dance floor"]:
        print(
            "You try to talk a bit but it's pretty loud and you don't get much across."
        )
        sleep(2)
        print("")
        print("One of them offers you some chewing gum.")
        print("     Do you want some chewing gum? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You take the chewing gum and put it in your pocket.")
            player.items.append(items["chewing gum"])
        elif option == False:
            print("You kindly turn down the offer.")
        player.NPCs["couple"].times_talked = 2
        return True
