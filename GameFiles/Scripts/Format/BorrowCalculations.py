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
