from .Calculations import create_list_people_in_room

item_redirect = {
    "a bottle of poppers": "your russian friend",
    "G": "the smile ambassador",
    "some special K": "your partner",
    "some chewing gum": "the attractive couple",
}


def available_borrows(player_obj):
    """Given the player object, returns a list of the current borrow actions
    that are available to the player depending to the "Ask for X" memories.
    Borrow gum doesnt require a memory"""

    final_list = []
    if "Ask for K" in player_obj.memories:
        final_list.append("your partner")
    if "Ask for G" in player_obj.memories:
        final_list.append("the smile ambassador")
    if "Ask for P" in player_obj.memories:
        final_list.append("your russian friend")
    if "Borrow Gum" in player_obj.memories:
        final_list.append("the attractive couple")

    return final_list


def remove_if_not_here(list_names_memories, player_obj):
    """una chapuza. Takes the list of names for available borrow memories (str)
    and the player object and returns a new list with the ones that are in the room"""
    ppl_here = create_list_people_in_room(player_obj)
    ppl_here_str = []
    memories_here_str = []

    for i in ppl_here:
        ppl_here_str.append(i.name)

    for i in list_names_memories:
        if i in ppl_here_str:
            memories_here_str.append(i)
            
    return memories_here_str
