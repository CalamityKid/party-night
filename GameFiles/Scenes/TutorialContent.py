from GameFiles.Scripts.Blocks.SceneSc import Scene
from GameFiles.Scripts.Format.Tutorial_input import player_choose_action_tutorial
from time import sleep


def tutorialcontent(player):
    original_act_dict = {}
    for key, act in player.dict_of_actions.items():
        original_act_dict[key] = act
    tutorial_actions = {"Talk": player.dict_of_actions["Talk"]}

    print("tutorial actions: ", tutorial_actions)
    player.dict_of_actions = tutorial_actions
    print("player ations rn: ", player.dict_of_actions)

    original_obj_dict = {}
    for key, obj in player.dict_of_objects.items():
        original_obj_dict[key] = obj
    tutorial_obj = {"partner": player.dict_of_objects["partner"]}
    player.dict_of_objects = tutorial_obj
    print("tutorial objects", tutorial_obj)
    print("player obj rn: ", player.dict_of_objects)

    print(
        "Okay, so, you're partying with your friends after a long time of no parties."
    )
    print(
        "You have no money and the idea is to have the best time you can with your friends."
    )
    sleep(4)

    print("You can perform actions by writing a verb and a noun.")
    act = None
    object = None
    print(player.dict_of_objects)
    while (act, obj) != ("talk to someone", "your partner"):
        print("""For example try "talk to partner". """)
        actin, objin = player_choose_action_tutorial(player)
        print("actin =", actin, "objin=", objin)
        act, obj = actin.name, objin.name
        print("act =", act, "obj =", obj)
    print("YOURE FREE")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    player.dict_of_actions = original_act_dict
    return None


tutorialscene = Scene("Tutorial", tutorialcontent)
"""
Talking with your friends is key to having a good time tonight. 
<<sleep 4>>
You can also use items you have in your pockets, they will affect how you feel. 
Some will give you a buzz, others will affect your breath and so on.
Try "smoke a cigarette", "smoke cig" works too.
<<run the thing, if detect is smoke and cigarette continue if not>> write "smoke a cigarette"

When you perform actions, they take time, usually 10 minutes.
The party will END and the game will be OVER at 6:00 AM.
<<sleep 6>>

There are three rooms in this party: the dance floor, the smoking room and the bathroom. 
You can move between them. The actions in each room will change slightly.
You are currently in the smoking room, try moving to the dance floor. 
<<run the thingy, detect move and dance floor to continue>>

Lastly, while on the dance floor, you can try dancing. Just write "dance".
Dancing can lead to different outcomes.
<<sleep 4>>
Let's pretend you're having a great time, you've smoked some weed and the music's great. 
<<set some stuff>>
Try writing "dance".
<<input thingy, only accepts dance>>. "try writing dance"

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
