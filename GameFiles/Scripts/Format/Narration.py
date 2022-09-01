from . import formatting
from .Calculations import create_list_people_in_room
from .BorrowCalculations import available_borrows, item_redirect


def narrate_items(player):
    unusable_item_list = []
    final_string = ""
    if len(player.items) == 0:
        final_string = "You don't have any items you can use atm."
    if len(player.items) > 0:
        final_string += "You can't use "
    for i in player.items:
        if i.usable_in_room(player.location) == False:
            unusable_item_list.append(i)

    if len(unusable_item_list) > 0:
        final_string += formatting.format_objects_string(unusable_item_list)
        final_string = final_string.replace("and", "or")
        final_string = final_string.replace(" a ", " the ")
        final_string = final_string.replace(".", " in this room though.")
    if len(player.items) > 0:
        print(
            "You have "
            + (formatting.format_objects_string(player.items)[:-1])
            + " in your pockets."
        )
    elif len(player.items) == 0:
        print("You're not holding anything rn.")
    if len(final_string) >= 34:
        print(final_string)


def narrate_actions(player):
    final_string = ""
    usable_actions = []
    for key, act in player.dict_of_actions.items():
        if act.doable_in_room(player.location) == True:
            usable_actions.append(act)
    final_string = formatting.format_objects_string(usable_actions)
    final_string = final_string.replace("and", "or")
    print("You could " + final_string)


def people_in_room_string(player_object):
    """takes player object, returns list of people in room as string"""
    return formatting.format_objects_string(create_list_people_in_room(player_object))
