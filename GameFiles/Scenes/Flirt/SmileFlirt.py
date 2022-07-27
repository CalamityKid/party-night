def smileflirtcontent(player):
    if player.NPCs["smile"].flirt > 0:
        print("You send each other air kisses.")
        return None
    elif player.NPCs["smile"].flirt == 0:
        print("You give them a long seductive look and a wink.")
        print("You're answered with a chuckle and a kiss on the cheek.")
        print("You both laugh it off.")
        player.NPCs["smile"].flirt += 1
        return None
