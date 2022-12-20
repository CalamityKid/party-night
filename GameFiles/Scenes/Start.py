from time import sleep
from GameFiles.Scripts.Blocks.SceneSc import Scene


def startcontent(player):
    print("")
    print("So, ", end="")
    sleep(2)
    print("you've come to this party with your partner")
    sleep(2)
    print("and two of your friends: ")
    sleep(2)
    print("""the self proclaimed "smile ambassador", """, end="")
    sleep(2)
    print("just type smile for short")
    sleep(1)
    print("and your russian friend.")
    sleep(4)
    print("")
    print("The party's pretty empty right now. ", end="")
    sleep(2)
    print("It'll get crowded later.")
    sleep(2)
    print("")
    print("You're pretty sober.", end="")
    sleep(2)
    print(" And broke.")
    sleep(2)
    print("")
    print("Let's see what the night brings...")
    sleep(2)
    print("")


startscene = Scene("Start", startcontent)
