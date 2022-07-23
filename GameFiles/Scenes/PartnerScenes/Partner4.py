from time import sleep

# only runs after 5 or after music changed, either way they're happy, gives you partnerLink Memory   [[|PartnerBank]]


def partnertimes4content(player):
    if "Partner Link" not in player.memories:
        print("you look at your partner")
        print("you weren't completely sure about coming out tonight")
        print("but just being here together is absolutely worth it")
        print("you consider you should start doing more things together")
        sleep(2)
        print("you're caught looking and get a smile back in return.")
        sleep(3)
        print("you're pretty sure this is what love feels like")
        sleep(2)
        player.modify_stat("lit", 10, True)
        player.modify_stat("coolness", 10, False)
        player.memories.append("PartnerLink")
        return True

    elif "Partner Link" in player.memories:
        return player.partnerscenes["PartnerBank"].run_scene(player)
