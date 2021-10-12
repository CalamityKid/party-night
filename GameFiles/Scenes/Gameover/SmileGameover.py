def smilegameovercontent(player):

    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|                                                            |")
    print("|           Oh, how to forget the smile ambassador?          |")

    if "Smile Link" in player.memories:
        print("|              never a boring day with this one              |")
    elif "Smile Link" not in player.memories:
        print("|               should have hung out more today              |")

    print("|                                                            |")
    if player.NPCs["smile"].times_talked > 2 and (
        player.NPCs["tanktop"] not in player.people_in_party
    ):
        print("|            You didn't meet their special friend            |")
        print("|                  well, maybe next time...                  |")
        print("|                                                             |")
    elif player.NPCs["smile"].times_talked > 2 and (
        player.NPCs["tanktop"] in player.people_in_party
    ):
        print("|             You got to meet their pusher friend            |")
        if "Pusher Business" in player.memories:
            print("|             which def worked out for both of you.          |")
        elif "Pusher Business" not in player.memories:
            print("|                   quite the character.                     |")
        print("|                                                            |")

    if "Smile Dance" in player.memories:
        print("|              Dancing together was stupid fun               |")
    elif "Smile Dance" not in player.memories:
        print("|             Wish you had danced together a bit             |")
    print("|     that fan's def gonna hurt someone eventually though    |")
    print("|                                                            |")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
