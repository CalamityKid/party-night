from time import sleep


def smilegameovercontent(player):

    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|                                                            |")
    print("|                                                            |")
    print("|           Oh, how to forget the smile ambassador?          |")

    if "Smile Link" in player.memories:
        print("|              never a boring day with this one              |")
        print("|             and today you got to hang out a lot            |")
    elif "Smile Link" not in player.memories:
        print("|               should have hung out more today              |")

    print("|                                                            |")
    sleep(2)
    if player.NPCs["smile"].times_talked > 2 and (
        player.NPCs["tanktop"] not in player.people_in_party
    ):
        print("|            You didn't meet their special friend            |")
        print("|                  well, maybe next time...                  |")
        print("|                                                            |")
        sleep(2)
    elif player.NPCs["smile"].times_talked > 2 and (
        player.NPCs["tanktop"] in player.people_in_party
    ):
        print("|             You got to meet their pusher friend            |")
        if "Pusher Business" in player.memories:
            print("|             which def worked out for both of you.          |")
        elif "Pusher Business" not in player.memories:
            print("|                   quite the character.                     |")
        print("|                                                            |")
        sleep(2)

    if "Smile Dance" in player.memories:
        print("|              Dancing together was stupid fun               |")
        print("|           the moniker is dumb af let's face it             |")
        print("|          but the smiles are def served everytime           |")
        print("|                                                            |")
        sleep(3)
    elif "Smile Dance" not in player.memories:
        print("|             Wish you had danced together a bit             |")
    print("|     that fan's def gonna hurt someone eventually though    |")
    sleep(2)
    print("|                                                            |")
    print("|                                                            |")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
    print("|/ \|\ /|/ \|\ /|/ \|\ /|/ \|\  /|/ \|\ /|/ \|\ /|/ \|\ /|/ \|")
