from time import sleep

# They appear in the room you're in when it becomes 00.30, its run by timed events
def coupletimes0content(player):
    print("What do you want to do? ", end="")
    input()
    print("")
    print("You were thinking about doing that but out of nowhere")
    print("")
    sleep(4)
    if player.location == player.rooms["smoking room"]:
        print("you see your friends, the cute couple, coming straight towards you.")
        print("")
        sleep(2)
        print("     Hey babes, sorry we're a bit late.")
        sleep(2)
        print("one of them says while the other one hugs your partner.")
        print("")
        sleep(3)
        print("     At least you made it, all the way from the mountains!")
        sleep(2)
        print("your friends live 30 minutes away from the city center")
        sleep(2)
        print("which is basically another continent.")
        print("")
        sleep(3)
        print("     Oh bitch, I think we all need some party after all this.")
        sleep(2)
        print("says one of them while the other one lights up a cigarette")
        sleep(2)
        print("nods all around, it's been too long for sure.")
        print("")
        sleep(3)

    elif player.location == player.rooms["dance floor"]:
        print("you see your friends, the cute couple, coming straight towards you.")
        print("")
        sleep(3)
        print("one of them says something while the other one hugs your partner")
        sleep(2)
        print("""you make out "sorry" and "late" over the music""")
        print("")
        sleep(3)

    elif player.location == player.rooms["bathroom"]:
        print("you see your friends, the cute couple, walk into the bathroom as well.")
        sleep(2)
        print("")
        print("     Hey babes, was going to look for you guys right now.")
        sleep(2)
        print(
            "one of them says while the other one blows you a kiss and goes into a stall."
        )
        print("")
        sleep(3)
        print("     At least you made it, hope you're not jetlagged.")
        sleep(2)
        print("your friends live 30 minutes away from the city center")
        sleep(2)
        print("so like, another country basically.")
        print("")
        sleep(3)
        print("     That's what the powder room's for babe, we're here to party today")
        sleep(2)
        print("you hear from the stall")
        sleep(2)
        print("while the other one is checks their hair on the mirror.")
        print("you all agree, you gonna party hard today.")
        print("")
        sleep(3)

    player.NPCs["partner"].location = player.location
    player.NPCs["couple"].location = player.location
    player.people_in_party.append(player.NPCs["couple"])
    player.NPCs["couple"].times_talked = 1
    return True
