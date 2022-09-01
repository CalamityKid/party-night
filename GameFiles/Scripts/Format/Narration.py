from . import formatting
from .Calculations import create_list_people_in_room


def narrate_actions(player_obj):
    final_string = ""
    useable_actions = []
    for key, act in player_obj.dict_of_actions.items():
        if act.doable_in_room(player_obj.location) == True:
            useable_actions.append(act)
    print(useable_actions)
    for i in useable_actions:
        i.narrate(player_obj)


def people_in_room_string(player_object):
    """takes player object, returns list of people in room as string"""
    return formatting.format_objects_string(create_list_people_in_room(player_object))
