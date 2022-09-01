from . import formatting
from .Calculations import create_list_people_in_room


def narrate_actions(player_obj):
    print("--------------------")
    player_obj.location.narrate()
    player_obj.dict_of_actions["Talk"].narrate(player_obj)
    print("AVAILABLE ACTIONS:")
    for key, act in player_obj.dict_of_actions.items():
        if key == "Talk" or key == "Use":
            continue

        else:
            if act.doable_in_room(player_obj.location) == True:
                act.narrate(player_obj)
    # print("You can always [TALK] to your partner.")
    print("---")
    player_obj.dict_of_actions["Use"].narrate(player_obj)
    print("--------------------")


def people_in_room_string(player_object):
    """takes player object, returns list of people in room as string"""
    return formatting.format_objects_string(create_list_people_in_room(player_object))
