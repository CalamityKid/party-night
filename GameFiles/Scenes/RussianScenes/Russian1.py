from ...Input import yesorno

# offers poppers
def russiantimes1content(player):
    if "Borrow" not in player.memories:
        print("Your russian friend tells you about this cool new metplix series.")
        return None

    elif "Borrow" in player.memories:
        option = False
        while option == False:
            print("     Baabes, I got some poppers on me alriight?")
            print("     You can [ASK] me for some whenever.")
            print("     Well, on the dance floor, not whenever.")
            print("     just let me know okaaay?")
            print("")
            print("     is it, okaaay? (y/n) ", end="")
            option = yesorno()
        print("You're okaaay with that.")
        print("")
        player.NPCs["russian"].times_talked = 2
        return True
