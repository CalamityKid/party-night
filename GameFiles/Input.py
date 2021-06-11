from .Scripts.Blocks.PlayerSc import MainCharacter, player
from .Scripts.Blocks.NPCSc import NPC, NPCs
from .Scripts.Blocks.RoomSc import rooms, Room
from .Scripts.Blocks.ItemsSc import items, Item
from .Scripts.Format import formatting


def player_choose_action(player):
    action_met = None
    while action_met == None:
        inputaction = None
        inputobject = None
        while (inputaction == None) or (inputobject == None):
            currentinput = input()
            try:
                print("current input: " + str(currentinput))
                inputaction, inputobject = formatting.format_input_command(currentinput)
                print(
                    "inside player_choose_action. after format_input."
                    + inputaction
                    + " + "
                    + inputobject
                )

            except TypeError:
                print(
                    "player choose action type error exception. Formar input didn't identify both an action and a object."
                )
                # input exceptions, this is for tap water, isn't an object
                if inputaction == player.dict_of_actions["Tap Water"]:
                    inputobject = True
                if inputobject == player.dict_of_actions["Tap Water"]:
                    inputaction = player.dict_of_actions["Tap Water"]
                    inputobject = True
                ###########################################input exception end

            print("action: " + str(inputaction) + "object: " + str(inputobject))
            if inputaction == None or inputobject == None:
                print("Try again, bitch. One of the things is None. It won't execute.")
                inputaction = None
                inputobject = None
        print("executing!")
        action_met = inputaction.execute(player, inputobject)
        if action_met == None:
            print(
                "execute returned None. So time doesn't pass. Try something else:, maybe here refresh available actions, also maybe a counter"
            )
