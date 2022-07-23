from ...Input import yesorno

# Tells you about introducing you to cutie, skips to introducing them if conditions are right
def russiantimes2content(player):
    if player.time.hour < 1:
        print("     Heey babes, there's a friend I wanted you to meet.")
        print("     Super cutie, you'll both like for suure.")
        print("     Haven't seen them around yet though.")
        print("")
        print("     Are you interested? (y/n) ", end="")
        option = yesorno()
        print("")
        if option == True:
            print("You're both looking forward to this mysterious cutie.")
        if option == False:
            print("You're like sure, we'll meet this person, whatever.")
        player.NPCs["russian"].times_talked = 3
        return True

    elif player.time.hour >= 1:
        if player.location == player.rooms["dance floor"]:
            print("     Heeey babes, I want you to meet my frieend.")
            print("Your russian friend introduces you to their friend.")
            print("It's a cutie in a tanktop.")
            print("")
            print("There's some smiling and flirting involved.")
            print("You partner gives you this look.")
            print("This wouldn't-mind-taking-them-home-with-us look.")
            player.people_in_party.append(player.NPCs["tanktop"])
            player.NPCs["tanktop"].location = player.location
            player.NPCs["russian"].times_talked = 4
            return True

        elif player.location != player.rooms["dance floor"]:
            print("     Baaabes, there's this friend. Super cute.")
            print("     Think you'll both like.")
            print("     I think they're already aroound?")
            print("     Will introduce you all later, for sure.")
            print("")
            print("     Are you interested? (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You're both looking forward to this mysterious cutie.")
            if option == False:
                print("You're like sure, I'll meet this person, whatever.")
            print("")
            player.NPCs["russian"].times_talked = 3
            return True
