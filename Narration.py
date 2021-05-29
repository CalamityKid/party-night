from Format import formatting


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
    print(final_string)
