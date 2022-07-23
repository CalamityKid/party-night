from random import randint

###################### BODY CHECK BARK
body_check_bark_dict = {
    0: "This is what's up now:",
    1: "This is what's popping:",
    2: "The lay of the land:",
    3: "Latest updates:",
    4: "Current party situation:",
    5: "STATUS:",
    6: "You connect to your inner being:",
    7: "You listen to your body:",
    8: "SITUATION REPORT:",
    9: "What had happened was:",
}


def body_check_bark():  ##Random opening statement before body check
    print(" ")
    op = randint(0, 9)
    print(body_check_bark_dict[op])
    return None


####################### FLIRT BARK


def flirt_bark_good(player):
    """Pass the player to it and though some randomizing and player stats it'll return a string saying that the flirt went well"""
    final_string_list = []
    final_string = ""


""" "title": "FlirtGoodBark(Person)",
		"tags": "flirt good bark",
		"body": ">><< random   0-2>>
<< if 0>> #active item
    <<if length of active items is 0>> "being clearheaded seems to help because"
    <<if length of active items is 1, select one>>
    <<if cig>> "maybe it's the nicotine but"
    <<if blunt>> "pure ganja suaveness,"
    <<if soundcloud>> "you're feeling joyful and it shows,"
    <<if coke>> "you get the twitch under control and"
    <<if specialK>> "the good vibes are felt,"
    <<if gum>> "minty fresh magic,"
    <<if lolipop>> "the lollipop complements the compliments,"
    <<if g>> "you're feeling relaxed and"
    <<if popp>> "you're still feeling a lightheaded but"


<< if 1>> #environment
    <<if player.location == bathroom>> "bathroom flirting,"
    <<if player.location == dance floor>> "the vibe of the dance floor helps,"
    <<if player.location == smoking room>> "it's quiet in here, it helps and"

<< if 2>> #stats
    <<random 0-2>>
    <<if 0>> "you're feeling cool,"
    <<if 1>> "the party feels more fun,"
    <<if 2>> "you start riding the wave and"

#second part
<<random 0-4>>
 <<if 0>> add " it goes well, you both smile."
 <<if 1>> add " you really nail it. Sparks fly."
 <<if 2>> add " you get the cutest smile in return."
 <<if 3>> add " you end up sounding charming as hell."
 <<if 4>> add " there's really good chemistry between you."

return 1 + 2
"""
