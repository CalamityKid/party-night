from ...Input import yesorno
from ...Scripts.Blocks import items

# Has just been introduced by russian friend at 1 am in the dance floor. Your partner is really into them.
def tanktoptimes0content(player):
    if player.location == player.rooms["dance floor"]:
        print("You can only half talk with the music this loud")
        print("so you end up giving each other looks and smiling")
        print("your partner's really going for it too")
        print("full on hunt mode")
        player.lit += 20
        player.NPCs["tanktop"].flirt += 1
        player.NPCs["tanktop"].times_talked = 1

    elif (
        player.location != player.rooms["dance floor"]
    ):  # should mean its later than 1 am y pasaste before
        print("The cutie in the tanktop smiles as you approach.")
        print("It's pretty damn charming.")
        print("")
        print("     It's nice to be able to party again, huh?")
        print("")
        print("and it's they way they say it")
        print("you can't help smiling back")
        player.lit += 20
        print("     Do you wanna try to flirt back? (y/n) ", end="")
        option = yesorno()
        if option == True:
            if items["blunt"] in player.active_items:  # you fuck it up
                if (
                    items["special K"] in player.active_items or player.cool > 40
                ):  # a half save
                    print("You respond with some corny line about good company")
                    print("they seem to like it")
                    player.NPCs["tanktop"].flirt += 1
                    return True
                print("You try to say something clever")
                print("but you're too stoned to nail it")
                print("it ends up sounding dumb but they don't seem to mind.")

            elif items["special K"] in player.active_items or player.cool > 40:
                print("You respond")
                print("     It'll be much nicer now that we get to party with you")
                print("")
                print("and you nail the delivery")
                print("")
                print("you can tell it worked")
                print("you're all smiling cheekily at each other")
                print("there's definitely tension")
                print("")
                player.NPCs["tanktop"].flirt += 2

        elif option == False:
            print("Your partner does flirt back. There's a chemistry.")
            print("")
        print("You talk for a few more minutes")
        print("a friend calls out to them")
        print("and they leave unwillingly.")
        player.NPCs["tanktop"].times_talked = 1
        return True
