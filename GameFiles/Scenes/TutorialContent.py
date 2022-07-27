from GameFiles.Scripts.Blocks.SceneSc import Scene
from GameFiles.Scripts.Format.Tutorial_input import player_choose_action_tutorial
from time import sleep


def tutorialcontent(player):
    print(player.dict_of_objects)
    print(player.dict_of_actions)

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

    print(
        "Okay, so, you're partying with your friends after a long time of no parties."
    )
    print(
        "You have no money and the idea is to have the best time you can with your friends."
    )
    sleep(4)
    ################### TALK
    print("You can perform actions by writing a verb and a noun.")
    act = None
    obj = None
    print(player.dict_of_objects)
    while (act, obj) != ("talk to someone", "your partner"):
        print("""For example try "talk to partner". """)
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name
    #################### USE
    print("Perfect!")
    sleep(2)
    print("Talking with your friends is key to having a good time tonight.")
    sleep(2)
    print(
        "You can also use items you have in your pockets, they will affect how you feel. "
    )
    print("Some will give you a buzz, others will affect your breath and so on.")
    player.dict_of_objects = {"cigarette": original_obj_dict["cigarette"]}
    player.dict_of_actions = {"Use": original_act_dict["Use"]}

    act = None
    obje = None
    print(player.dict_of_objects)
    while (act, obj) != ("use something you're holding", "a cigarette"):
        print("""You can "take" or "use" or "smoke" different things you find.""")
        print("""Try "smoke a cigarette", "smoke cig" works too.""")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name

    print("That's it!")
    sleep(2)
    print("You can only use items in your pockets.")
    print("You'll get your hands on different things as the night goes on.")
    sleep(3)
    ################ MOVE
    print("")
    print("It's 12 am right now. The party ends at 6 am.")
    sleep(1)
    print("As you perform different actions, time will pass.")
    print("Actions usually take about 10 minutes.")
    sleep(2)
    print("Life is full of surprises though, who knows what will happen?")
    sleep(2)
    print("")
    print("")
    print(
        "There are three rooms in this party: the dance floor, the smoking room and the bathroom."
    )
    print("You can move between them. The actions in each room will change slightly.")
    player.dict_of_objects = {
        "smoking room": original_obj_dict["smoking room"],
        "bathroom": original_obj_dict["bathroom"],
        "dance floor": original_obj_dict["dance floor"],
    }
    player.dict_of_actions = {"Move": original_act_dict["Move"]}

    act = None
    obj = None
    print(player.dict_of_objects)
    while (act, obj) != ("move somewhere else", "the dance floor"):
        print("You are currently in the smoking room, try moving to the dance floor. ")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name

    print("Perfect, that's how you move!")
    sleep(2)
    ################### DANCE
    print("Lastly, while on the dance floor, you can try dancing.")
    print("""Just write "dance".""")
    print("")
    sleep(3)
    print("Dancing can lead to different outcomes.")
    sleep(2)
    print("Let's pretend you're having a great time,")
    print("you've smoked some weed and the music's great.")
    sleep(2)
    player.lit = 100
    player.coolness = 0
    player.mouth = 100
    player.high = 60
    player.dict_of_objects = {}
    player.dict_of_actions = {"Dance": original_act_dict["Dance"]}

    act = None
    obj = None
    print(player.dict_of_objects)
    while (act, obj) != ("dance", True):
        print("""Try writing "dance" now.""")
        actin, objin = player_choose_action_tutorial(player)
        act, obj = actin.name, objin.name
        print("")

    act.execute(player, None)
    print("")
    print("")

    player.dict_of_actions = original_act_dict
    player.dict_of_objects = original_obj_dict
    player.people_in_party = original_ppl
    return None


tutorialscene = Scene("Tutorial", tutorialcontent)
# return lit, high etc to initial ones after
"""
  
If you don't like the music, are too sober or not enjoying the party it'll go worse.
<<sleep 4>>
Let's "dance again"
<<set some shit>>
<<do it again>>

When you feel people are looking at you, it can make you self conscious.
It gives you performance anxiety.
<<sleep 5>>

If your friends are on the dance floor with you, it'll help ease it.
The closer to your friends are, the less anxious you'll feel when they're by your side.
So remember to talk to your friends.
<<sleep 4>>
Let's try dance one last time.
<<set some shit>>
<<do it again>>

Cool. That's the end of the tutorial! Let's get to the game.
return Beggining"""
