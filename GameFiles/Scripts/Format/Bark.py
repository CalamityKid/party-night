from random import randint, choice
from ...Scenes.Flirt.GoodBarkText import (
    no_item_string,
    good_bark_item_string_dict,
    body_check_bark_dict,
    good_bark_room_string_dict,
    good_bark_stats_string_dict,
    ending_string_dict,
)
from ...Scenes.Flirt.BadBarkText import (
    bad_no_item_string,
    bad_bark_item_string_dict,
    bad_bark_room_string_dict,
    bad_bark_stats_string_dict,
    bad_ending_string_dict,
)

# The text is in the BarkText files in the Flirt Scenes


def body_check_bark():  ##Random opening statement before body check
    """prints a randomized opening statement before a body check"""
    op = randint(0, 9)
    print(body_check_bark_dict[op])
    return None


### GOOD BARK
def flirt_bark_good(player_obj):
    """Pass the player to it and though some randomizing and current stats it'll return a string saying that the flirt went well"""
    final_string_list = []
    final_string = ""
    randselect = randint(0, 2)

    if randselect == 0:  # active item select
        if len(player_obj.active_items) == 0:
            final_string_list.append(no_item_string)

        elif len(player_obj.active_items) > 0:
            randitem = choice(list(player_obj.active_items.keys()))
            final_string_list.append(good_bark_item_string_dict[randitem])

    elif randselect == 1:  # room
        final_string_list.append(good_bark_room_string_dict[player_obj.location.name])

    elif randselect == 2:  # stats
        randstat = randint(0, 2)
        final_string_list.append(good_bark_stats_string_dict[randstat])

    # second sentence
    randending = randint(0, 4)
    final_string_list.append(ending_string_dict[randending])
    final_string = "".join(final_string_list)
    return final_string


###BAD BARK
def flirt_bark_bad(player_obj):
    """Pass the player to it and though some randomizing and current stats it'll return a string saying that the flirt went badly"""
    final_string_list = []
    final_string = ""
    randselect = randint(0, 2)

    if randselect == 0:  # active item select
        if len(player_obj.active_items) == 0:
            final_string_list.append(bad_no_item_string)

        elif len(player_obj.active_items) > 0:
            randitem = choice(list(player_obj.active_items.keys()))
            final_string_list.append(bad_bark_item_string_dict[randitem])

    elif randselect == 1:  # room
        final_string_list.append(bad_bark_room_string_dict[player_obj.location.name])

    elif randselect == 2:  # stats
        randstat = randint(0, 2)
        final_string_list.append(bad_bark_stats_string_dict[randstat])

    # second sentence
    randending = randint(0, 4)
    final_string_list.append(bad_ending_string_dict[randending])
    final_string = "".join(final_string_list)
    return final_string
