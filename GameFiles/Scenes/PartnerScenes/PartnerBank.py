from time import sleep
from ...Scripts.Blocks import items


def partnerbankcontent(player):

    if hasattr(player, "banklist") == False:
        player.banklist = ["keta", "GHB", "fun", "mouth", "empty", "reloaded"]

    if "keta" in player.banklist:
        if (
            items["special K"] not in player.active_items
            and player.high < 50
            and player.NPCs["partner"].kusesleft > 1
        ):
            print("    Remember I have some k left in case you want some.")
            print("")
            sleep(2)
            print("you make a point to ask for some")
            sleep(1)
            print("if you feel like it later")
            player.banklist.remove("keta")
            return False

    if "GHB" in player.banklist:
        if items["G"] not in player.active_items and player.high < 50:
            print("    We can always ask for some G")
            sleep(2)
            print("    if you're too sober")
            sleep(2)
            print("")
            print("you make a point to ask your friend")
            sleep(2)
            print("the smile ambassador for some later")
            sleep(2)
            print("if you feel like it")
            player.banklist.remove("GHB")
            return False

    if "fun" in player.banklist:
        if player.lit < 30:
            print("    You don't seem like you're having fun babe")
            sleep(2)
            print("    Let's go talk with our friends")
            sleep(2)
            print("    or dance a bit")
            print("")
            sleep(2)
            print("you might as well")
            timestr = "it's only " + str(player.time)
            print(timestr)
            player.modify_stat("lit", 10, True)
            print("")
            player.banklist.remove("fun")
            return False

    if "mouth" in player.banklist:
        if player.mouth < 30:
            print("    My mouth's so dry, isn't yours?")
            sleep(2)
            print("    Maybe we should try to get a lollipop")
            sleep(2)
            print("    or some chewing gum or something")
            sleep(2)
            print("")
            print("we could always drink tap water too")
            sleep(2)
            print("if we need water bad")
            player.banklist.remove("mouth")
            return False

    if "empty" in player.banklist:
        if player.NPCs["partner"].kusesleft == 0 and player.high < 50:
            print("    I wish I had some k left...")
            print("")
            print("you can't help laughing")
            player.modify_stat("lit", 10, True)
            player.banklist.remove("empty")
            return False

    if "reloaded" in player.banklist:
        if "Commission" in player.memories:
            print("     What a wonderful night")
            sleep(2)
            print("     meeting this total cutie")
            sleep(2)
            print("     and we even got some more k")
            sleep(2)
            print("")
            print("this unbridled love for horse tranquilizer")
            sleep(2)
            print("you let out a laugh")
            print("")
            player.modify_stat("lit", 10, True)
            player.banklist.remove("reloaded")
            return False

    if "Partner Link" not in player.memories:
        print("they wish they were dancing")
        return False

    elif "Partner Link" in player.memories:
        print("you're really grateful to be sharing your life with your partner ")
        sleep(2)
        print("you stay in quiet appreciation")
        return False
