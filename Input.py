from Blocks.PlayerNPC import (
    setupcharacters,
    player,
    NPC,
    MainCharacter,
)
from Blocks.Room import rooms, Room
from Blocks.Items import items, Item

NPCs = setupcharacters()


def yesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = yesornoresult.lower()
            if "y" in yesornoresult[0]:
                return True
            elif "n" in yesornoresult[0]:
                return False
        print("(yes or no):", end=" ")
        yesornoresult = None


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
all_actions = create_dictionary_of_items(rooms, rooms, items)


def identify_object(object_to_be_identified_list, dict_of_objects):
    for word in object_to_be_identified_list:
        if word == "g":
            return items["G"]
        for objectx in dict_of_objects:
            for identifierx in dict_of_objects[objectx].identifiers:
                if identifierx in word:
                    return dict_of_objects[objectx]


def identify_action(action_to_be_identified, dict_of_actions):
    for objectx in dict_of_actions:
        for identifierx in dict_of_actions[objectx].identifiers:
            if identifierx in action_to_be_identified:
                return dict_of_actions[objectx]


def clean_input(to_clean):
    result = None
    if type(to_clean) == str:
        result = to_clean.lower()
        result = result.strip()
        return result
    elif type(to_clean) != str:
        print("clean_input wasn't fed a string.")
        return None


def format_input_command(
    player_input, dict_of_actions=all_actions, dict_of_objects=all_objects
):
    action = None
    subject = None
    player_input = clean_input(player_input)
    player_input = player_input.split()
    action = player_input[0]
    subject = player_input[1:]
    print("before running the functions", action, subject)
    #####################################################################
    action = identify_action(action, dict_of_actions)
    print("return of action function: ", action)
    if action == None:
        print("action returned None")
        return None
    #######################################################################
    subject = identify_object(subject, dict_of_objects)
    print("return of subject function: ", subject)
    if subject == None:
        print("subject returned None")
        return None
    print(action, subject)
    return action, subject


x = input()
format_input_command(x)
