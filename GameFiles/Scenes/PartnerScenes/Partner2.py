from time import sleep
from .Compile import partnerscenes

# appreciation and some navi stuff
# in order to get to 3, you have to dance after boost is more than 1.3


def partnertimes2content(player):
    if player.NPCs["partner"].boost < 1.3:
        print("who's looking very pleased just by being here")
        print("and it's a really good look")
        sleep(2)
        print("you appreciate what a beautiful creature your partner is")
        sleep(1)
        print("you're caught looking and get the most charming smile in return")
        sleep(2)
        player.NPCs["partner"].boost = 1.3
        return False
    else:
        print("your partner tells you")
        return partnerscenes["PartnerBank"].run_scene(player)
