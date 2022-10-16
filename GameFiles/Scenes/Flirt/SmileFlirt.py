from tiem import sleep


def smileflirtcontent(player):
    if player.NPCs["smile"].flirt > 0:
        print("You send each other air kisses.")
        return None
    elif player.NPCs["smile"].flirt == 0:
        print("You give them a long seductive look and a wink.")
        sleep(1)
        print("You're answered with a chuckle and a kiss on the cheek.")
        sleep(1)
        print("You both laugh it off.")
        player.NPCs["smile"].flirt += 1
        return None
