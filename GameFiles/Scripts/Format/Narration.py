from . import formatting
from .Calculations import create_list_people_in_room


def narrate_actions(player_obj):
    print("--------------------")
    print("AVAILABLE ACTIONS:")
    for key, act in player_obj.dict_of_actions.items():
        if act.doable_in_room(player_obj.location) == True:
            act.narrate(player_obj)
    print("You can always [TALK] to your partner.")
    print("--------------------")


def people_in_room_string(player_object):
    """takes player object, returns list of people in room as string"""
    return formatting.format_objects_string(create_list_people_in_room(player_object))
