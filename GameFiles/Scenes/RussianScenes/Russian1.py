from time import sleep
from ...Input import yesorno

# offers poppers
def russiantimes1content(player):
    if "Ask for K" not in player.memories:
        print("who tells you about this cool new metplix series.")
        sleep(2)
        print("")
        print("Your partner seems to want to tell you something.")
        return None

    elif "Ask for K" in player.memories:
        option = None
        print("who turns to your and your partner and says")
        sleep(1)
        print("")
        print("     Baabes, ", end="")
        sleep(2)
        print("I got some poppers on me, by the wayy.")
        sleep(2)
        print("     You can ask me for some whenever.")
        sleep(2)
        print("     Well, ", end="")
        sleep(1)
        print("on the dance floor, ", end="")
        sleep(1)
        print("not whenever.")
        sleep(1)
        print("     just let me know ", end="")
        sleep(1)
        print("if you want some ", end="")
        sleep(1)
        print("okaaay?")
        print("")
        while option != True:
            print("     Did you get that? (y/n) ", end="")
            option = yesorno()
            if option == False:
                print("     I mean, like ASK me if you want some.")
                sleep(1)
                print("")
        print("You got it okaaay.")
        player.NPCs["russian"].times_talked = 2
        player.memories.append("Ask for P")
        return True
