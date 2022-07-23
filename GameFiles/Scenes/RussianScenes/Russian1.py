from ...Input import yesorno

# offers poppers
def russiantimes1content(player):
    if "Ask for K" not in player.memories:
        print("Your russian friend tells you about this cool new metplix series.")
        return None

    elif "Ask for K" in player.memories:
        option = None
        print("     Baabes, I got some poppers on me alriight?")
        print("     You can ask me for some whenever.")
        print("     Well, on the dance floor, not whenever.")
        print("     just let me know okaaay?")
        print("")
        while option != True:
            print("     Did you get that? (y/n) ", end="")
            option = yesorno()
            if option == False:
                print("     I mean, like ASK me if you want some.")
                print("")
        print("You got it okaaay.")
        print("")
        player.NPCs["russian"].times_talked = 2
        player.memories.append("Ask for P")
        return True
