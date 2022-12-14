from random import randint
from time import sleep

# theyve already told you about introducing you, youre stuck here until you meet


def russiantimes3content(player):
    if player.location == player.rooms["dance floor"]:
        if player.time.hour >= 1:
            print("     Heeey babes, I want you to meet my frieend.")
            sleep(2)
            print("Your russian friend introduces you to their friend.")
            sleep(2)
            print("It's a cutie in a tanktop.")
            sleep(2)
            print("")
            print("There's some smiling and flirting involved.")
            sleep(2)
            print("You partner gives you this look.")
            sleep(2)
            print("This wouldn't-mind-taking-them-home-with-us look.")
            player.people_in_party.append(player.NPCs["tanktop"])
            player.NPCs["tanktop"].location = player.location
            player.NPCs["russian"].times_talked = 4
            return True

        elif player.time.hour < 1:
            op = randint(0, 2)
            if op == 0:
                print("Self isolation though music and poppers, a thesis in action.")
            elif op == 1:
                print("The argument for contemplative dancing, peace in the crowd.")
            elif op == 2:
                print("You try, but you can't reach them in their dance dimension. ")
            print("you decide to try again later.")
            return None

    elif player.location != player.rooms["dance floor"]:
        print("You talk about this movie you both watched recently.")
        return None
