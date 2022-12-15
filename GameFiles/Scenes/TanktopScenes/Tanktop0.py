from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks import items


# Has just been introduced by russian friend at 1 am in the dance floor. Your partner is really into them.
def tanktoptimes0content(player):
    if player.location == player.rooms["dance floor"]:
        print("You can only half talk with the music this loud")
        sleep(1)
        print("so you end up giving each other looks and smiling")
        sleep(2)
        print("your partner's really going for it too")
        sleep(1)
        print("full on hunt mode")
        player.lit += 20
        player.NPCs["tanktop"].flirt += 1
        player.NPCs["tanktop"].times_talked = 1
        print("")
        sleep(2)
        return True

    elif (
        player.location != player.rooms["dance floor"]
    ):  # should mean its later than 1 am y pasaste before
        print("The cutie in the tanktop smiles as you approach.")
        sleep(1)
        print("It's pretty damn charming.")
        print("")
        sleep(2)
        print("     It's nice to be able to party again, huh?")
        sleep(2)
        print("")
        print("and it's they way they say it")
        sleep(1)
        print("you can't help smiling back")
        player.lit += 20
        print("")
        sleep(2)

        print("     Do you wanna try to flirt back? (y/n) ", end="")
        option = yesorno()
        if option == True:
            if items["blunt"] in player.active_items:  # you fuck it up
                if (
                    items["special K"] in player.active_items or player.cool > 40
                ):  # a half save
                    print("You respond with some corny line about good company")
                    sleep(2)
                    print("they seem to like it")
                    player.NPCs["tanktop"].flirt += 1
                    sleep(2)
                    return True
                print("You try to say something clever")
                sleep(2)
                print("but you're too stoned to nail it")
                sleep(2)
                print("it ends up sounding dumb but they don't seem to mind.")

            elif items["special K"] in player.active_items or player.coolness > 40:
                print("You respond")
                print("     It'll be much nicer now that we get to party with you")
                print("")
                sleep(2)
                print("and you nail the delivery")
                print("")
                sleep(2)
                print("you can tell it worked")
                sleep(2)
                print("you're all smiling cheekily at each other")
                sleep(2)
                print("there's definitely tension")
                print("")
                player.NPCs["tanktop"].flirt += 2

        elif option == False:
            print("Your partner does flirt back. There's a chemistry.")
            print("")
            sleep(2)
        print("You talk for a few more minutes")
        sleep(2)
        print("a friend calls out to them")
        sleep(2)
        print("and they leave unwillingly.")
        print("")
        player.NPCs["tanktop"].times_talked = 1
        return True
