from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks import items
from ...Scripts.Actions import use_item

# divinity


def russiantimes5content(player):
    if "Russian Link" not in player.memories:
        if player.location == player.rooms["dance floor"]:
            print("Music's pretty loud, hard to talk.")
            return None

        elif player.location != player.rooms["dance floor"]:
            print("     Baabes, you having fuun?")
            sleep(2)
            print("Your partner says it is definitely quite the night.")
            sleep(2)
            print("They start talking amongst themselves.")
            print("")
            print("You start to think how much you value this friendship.")
            print("")
            print("     You okay with pda? (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You hug your russian friend and kiss their forehead.")
            elif option == False:
                print("You kinda just stand there and enjoy the moment.")
            print("")
            sleep(2)
            if "Attending Film Festival" in player.memories:
                print(
                    "You're looking forward to this film festival thing next weekend."
                )
            elif "Not Attending Film Festival" in player.memories:
                print("Maybe you'll reconsider the whole film festival thing later.")
            sleep(2)
            print("You know you'll remember this moment fondly.")
            player.memories.append("Russian Link")
            return True

    elif "Russian Link" in player.memories:
        if player.location == player.rooms["bathroom"]:
            if "Divinity" in player.memories:
                print("You comment about how divine this red haired")
                sleep(2)
                print("coke wielding wonder was.")
                sleep(2)
                print("This a fairy entity.")
                sleep(2)
                print("What a moment.")
                return None

            elif "Divinity" not in player.memories:
                print("Your russian friend is talking to this high heeled")
                sleep(2)
                print("like, lucious red curly hair-up-to-their-waist")
                sleep(2)
                print("big breasted, full lipped, cheekbones-for-days divinity.")
                print("")
                sleep(2)
                print("They introduce you and your partner to them")
                sleep(2)
                print("and you tell them how absolutely stunning they are")
                sleep(2)
                print("and they say thanks, thanks")
                print("")
                sleep(3)

                print("and also they offer you some coke.")
                print("")
                print("     Do you want some coke? (y/n) ", end="")

                option = yesorno()
                if option == True:
                    print("You gracefully accept.")
                    player.items.append(items["coke"])
                    use_item.execute(player, items["coke"])
                elif option == False:
                    print("You turn it down. Your partner does take some.")

                print("")
                sleep(2)
                print("They say they were just leaving.")
                print("")
                print("     Absolute pleasure sweethearts, see you next time.")
                sleep(2)
                print("gives each of you one kiss on each cheek ")
                sleep(2)
                print("and leaves")
                print("")
                print("It's feels kinda surreal")
                sleep(2)
                print("a bit like you dreamt it")
                sleep(2)
                print("You're kinda blown away by the whole experience.")
                player.memories.append("Divinity")
                return True

        elif player.location != player.rooms["bathroom"]:
            print("You feel really glad your russian friend is in your lives.")
            return None
