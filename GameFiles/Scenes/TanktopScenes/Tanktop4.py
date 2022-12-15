from random import randint
from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks import items

# Candy's kicked in now, you have to dance with them to jump to 5, if not on dance floor you can get a cigarette, maybe flirt and they go to the dance floor again
def tanktoptimes4content(player):
    if player.location == player.rooms["dance floor"]:
        print("You approach the cutie in the tanktop's group of friends")
        sleep(1)
        print("and they're all really getting down to the music.")
        sleep(2)
        print("You can't really talk, they're all movement.")
        print("")
        return None

    elif player.location != player.rooms["dance floor"]:
        print("You approach the cutie in the tanktop's group of friends.")
        sleep(1)
        print("The cutie's smoking a cigarette, most of them are.")
        sleep(1)
        print("They offer you one.")
        print("")
        print("     Do you want a cigarette? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You accept the cigarette.")
            player.items.append(items["cigarette"])
        elif option == False:
            print("You offhandedly refuse the offer.")

        sleep(1)

        if "Tanktop Conversation" in player.memories:
            print("You can feel your partner holding back.")
            print("")

        elif "Tanktop Interest" in player.memories:
            print("You talk about random stuff.")
            sleep(2)
            print("Things seem more interesting when being told by a hottie.")
            sleep(2)
            print("You get some compliments in.")

            op = randint(0, 2)
            if op == 1:
                print("You focus on the way they play with their cigarette.")
            elif op == 1:
                print("You focus on that beautiful smile.")
            elif op == 1:
                print("You love how your partner is really going for it.")
                sleep(2)
                print("They get along great, it's really cute.")
                player.NPCs["tanktop"].flirt += 1
            sleep(1)
        elif "Tanktop Partner" in player.memories:
            print("Your partner gets some sexy energy into the conversation.")
            sleep(2)
            print("Yeah, there's chemistry for sure.")

        print(
            "When everybody's done with their cigarette they decide to go back to the dance floor."
        )
        sleep(2)
        print("The cutie lets you know they'll all be downstairs dancing.")
        print("")
        player.NPCs["tanktop"].location = player.rooms["dance floor"]
        return True
