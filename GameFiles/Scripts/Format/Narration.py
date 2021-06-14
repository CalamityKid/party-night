from typing import final
from . import formatting


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

    final_string += formatting.format_objects_string(unusable_item_list)
    final_string = final_string.replace("and", "or")
    final_string = final_string.replace(" a ", " the ")
    final_string = final_string.replace(".", " in this room though.")
    print("You're holding " + formatting.format_objects_string(player.items))
    if len(final_string) >= 34:
        print(final_string)


def narrate_people_in_room(player):
    people_in_room_string = ""
    people_in_room_list = []
    for key, person in player.dict_of_people.items():
        if person.location == player.location:
            people_in_room_list.append(person)
    people_in_room_string = formatting.format_objects_string(people_in_room_list)
    if people_in_room_string == "nothing":
        people_in_room_string = "no familiar faces."
    player.location.narrate()
    print("You see", people_in_room_string)
    if people_in_room_string != "no familiar faces.":
        print("You could [TALK] to them.")


def narrate_actions(player):
    final_string = ""
    usable_actions = []
    for key, act in player.dict_of_actions.items():
        if act.doable_in_room(player.location) == True:
            usable_actions.append(act)
    final_string = formatting.format_objects_string(usable_actions)
    final_string = final_string.replace("and", "or")
    print("You could " + final_string)