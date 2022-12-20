from GameFiles.Scripts.Blocks.SceneSc import Scene
from GameFiles.Scripts.Format.Tutorial_input import (
    player_choose_action_tutorial,
    yesorno,
)
from time import sleep


def tutorialcontent(player):

    original_act_dict = {}
    for key, act in player.dict_of_actions.items():
        original_act_dict[key] = act
    tutorial_actions = {"Talk": player.dict_of_actions["Talk"]}

    player.dict_of_actions = tutorial_actions

    original_obj_dict = {}
    for key, obj in player.dict_of_objects.items():
        original_obj_dict[key] = obj
    tutorial_obj = {"partner": player.dict_of_objects["partner"]}
    player.dict_of_objects = tutorial_obj

    original_ppl = []
    for person in player.people_in_party:
        original_ppl.append(person)
    player.people_in_party = []

    or_lit = player.lit
    or_high = player.high
    or_cool = player.coolness
    or_mouth = player.mouth

    print("Okay, so, you're partying with your friends", end=" ")
    sleep(2)
    print("after a long time of no parties.")
    sleep(3)
    print("You have no money", end=" ")
    sleep(2)
    print("but you'll make the most out of tonight.")
    sleep(3)
    print("")
    print("Try to have the best time you can with your friends.")
    sleep(3)
    print("")
    ################### TALK
    print("You can perform actions by writing a verb and a noun.")
    sleep(2)
    act = None
    obj = None

    while (act, obj) != ("talk to someone", "your partner"):
        print("""For example try "talk to partner". """)
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name
    #################### USE
    print("Perfect!")
    sleep(2)
    print("Talking with your friends is key to having a good time tonight.")
    sleep(3)
    print("")
    print(
        "You can also use items you have in your pockets, they will affect how you feel. "
    )
    sleep(2)
    print("Some will give you a buzz, others will affect your breath and so on.")
    sleep(3)
    print("")
    player.dict_of_objects = {"cigarette": original_obj_dict["cigarette"]}
    player.dict_of_actions = {"Use": original_act_dict["Use"]}

    act = None
    obje = None

    while (act, obj) != ("use something you're holding", "a cigarette"):
        print("""You can "take" or "use" or "smoke" different things you find.""")
        print("""Try "smoke a cigarette", "smoke cig" works too.""")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name

    print("That's it!")
    sleep(2)
    print("")
    print("You can only use items in your pockets.")
    sleep(2)
    print("You'll get your hands on different things as the night goes on.")
    sleep(4)
    ################ MOVE
    print("")
    print("You get to the party at 12 am. It will end at 6 am.")
    sleep(3)
    print("As you perform different actions, time will pass.")
    print("Actions usually take about 10 minutes.")
    sleep(4)
    print("")
    print("Life is full of surprises though, who knows what will happen?")
    sleep(3)
    print("")
    print("")
    print("There are three rooms in this party:")
    sleep(3)
    print("the dance floor,", end=" ")
    sleep(2)
    print("the smoking room", end=" ")
    sleep(2)
    print("and the bathroom.")
    sleep(2)
    print("You can move between them. The actions in each room will change slightly.")
    print("")
    sleep(3)
    player.dict_of_objects = {
        "smoking room": original_obj_dict["smoking room"],
        "bathroom": original_obj_dict["bathroom"],
        "dance floor": original_obj_dict["dance floor"],
    }
    player.dict_of_actions = {"Move": original_act_dict["Move"]}

    act = None
    obj = None

    while (act, obj) != ("move somewhere else", "the dance floor"):
        print("You are currently in the smoking room, try moving to the dance floor. ")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name

    print("Perfect, that's how you move!")
    print("")
    sleep(2)
    ################### DANCE
    player.location = player.rooms["dance floor"]
    print("Now, let's talk about", end="")
    sleep(2)
    print(" dancing.")
    sleep(1)
    print("While on the dance floor, you can try to dance.")
    sleep(2)
    print("""Just write "dance".""")
    print("")
    sleep(3)
    print("Dancing can lead to different outcomes.")
    sleep(3)
    print("Let's pretend you're having a great time,")
    sleep(2)
    print("you've smoked some weed and the music's great.")
    print("")
    sleep(4)
    player.lit = 100
    player.coolness = 0
    player.mouth = 100
    player.high = 60

    player.dict_of_objects = {}
    player.dict_of_actions = {"Dance": original_act_dict["Dance"]}

    act = None
    obj = None

    while (act, obj) != ("dance", True):
        print("""Try writing "dance" now.""")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin
        print("")

    actin.execute(player, None)
    print("")
    sleep(4)
    print("Okay!", end=" ")
    sleep(2)
    print("That went well!")
    sleep(2)
    print("")
    print("If you don't like the music though,")
    sleep(3)
    print("or if you're too sober or not enjoying the party it'll go worse.")
    sleep(2)
    print("So let's try that again. This time though...")
    print("")
    sleep(4)

    player.lit = 10
    player.coolness = 50
    player.mouth = 50
    player.high = 10

    player.narrate_stats(False)
    sleep(2)

    act = None
    obj = None

    while (act, obj) != ("dance", True):
        print("Let's dance again.")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin
        print("")

    actin.execute(player, None)
    sleep(4)
    print("Yeah...", end=" ")
    sleep(3)
    print("That didn't go so well.")
    sleep(3)
    print("")
    print("When you feel people are looking at you,", end=" ")
    sleep(2)
    print("it can make you self conscious.")
    sleep(3)
    print("It gives you performance anxiety.")
    sleep(4)
    print("")
    print("If your friends are on the dance floor with you,", end=" ")
    sleep(3)
    print("it'll help ease it.")
    print("")
    sleep(3)
    print("The closer to your friends you are,", end=" ")
    sleep(2)
    print("the less anxious you'll feel when they're by your side.")
    sleep(1)
    print("")
    print("So remember to talk to your friends.")
    sleep(4)
    print("")
    print("""Lastly, you can "Check" different things""", end=" ")
    sleep(3)
    print("like your pockets, the party, the time...")
    sleep(3)
    print("You can even Check yourself", end=" ")
    sleep(3)
    print("to see how you're feeling")
    sleep(4)
    print("so don't forget the check command, it can be useful.")
    sleep(4)
    print("")
    print("Anyway, that was it for the tutorial.")
    print("     Did you get all that? (y/n)", end=" ")
    op = yesorno()
    if op == True:
        print("Wonderful, then you're ready!")
    elif op == False:
        print("You'll figure it out, I'm sure...")
    sleep(4)
    print("You can repeat the tutorial again at any time by writing TUTORIAL.")
    sleep(4)
    print("Now back to the game!")
    sleep(4)
    print("")

    player.dict_of_actions = original_act_dict
    player.dict_of_objects = original_obj_dict
    player.people_in_party = original_ppl
    player.high = or_high
    player.coolness = or_cool
    player.lit = or_lit
    player.mouth = or_mouth
    return None


tutorialscene = Scene("Tutorial", tutorialcontent)
