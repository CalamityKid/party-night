from .Scripts.Blocks.PlayerSc import MainCharacter, player
from .Scripts.Blocks.NPCSc import NPC, NPCs
from .Scripts.Blocks.RoomSc import rooms, Room
from .Scripts.Blocks.ItemsSc import items, Item
from .Scripts.Format import formatting
from .Scripts.Actions import dict_of_actions, Move


def create_dictionary_of_items(dict1, dict2, dict3):
    dictionary_of_items = {}
    for key, value in dict1.items():
        dictionary_of_items[key] = value
    for key, value in dict2.items():
        dictionary_of_items[key] = value
    for key, value in dict3.items():
        dictionary_of_items[key] = value
    return dictionary_of_items


all_objects = create_dictionary_of_items(items, rooms, NPCs)


def player_choose_action():
    action_met = None
    while action_met == None:
        inputaction = None
        inputobject = None
        while (inputaction == None) or (inputobject == None):
            currentinput = input()
            try:
                inputaction, inputobject = formatting.format_input_command(
                    currentinput, dict_of_actions, all_objects
                )
            except TypeError:
                #input exceptions, this is for tap water, isn't an object
                ###########REVISAR ESTO
                if inputaction == dict_of_actions["Tap Water"]:
                    inputobject = True
                #############    
                if inputaction == None or inputobject == None:
                print("Try again, bitch.")
                inputaction = None
                inputobject = None
        action_met = inputaction.execute(player, inputobject)
        if action_met == None:
            print(
                "That ain't nothing bitch, try something else:, maybe here refresh available actions, also maybe a counter"
            )
