def create_list_people_in_room(player):
    people_in_room_list = []
    for person in player.people_in_party:
        if person.location == player.location:
            people_in_room_list.append(person)
    return people_in_room_list


def calculate_friend_boost(player):
    total_boost = 0
    people_in_room = create_list_people_in_room(player)
    for person in people_in_room:
        total_boost += person.boost
    print("total boost is", total_boost)
    return int(total_boost * 10)


def calculate_mod_item_effect(player, variable_in_string):
    mod_name = str(variable_in_string) + ("_mod")
    total = 0
    count = 0
    base_stat = getattr(player, variable_in_string)
    print("created mod name", mod_name)
    for item, effect in player.active_items.items():
        print(item, ":")
        if hasattr(item, mod_name) == True:
            total += (base_stat * ((getattr(item, mod_name)))) - base_stat
            count += 1
    if count > 0:
        print(
            variable_in_string,
            "base is",
            base_stat,
            "the mod is returning",
            int((base_stat + total)),
        )
        print("")
        return int((base_stat + total))
    elif count == 0:
        print(variable_in_string, "isnt modded, returns", base_stat)
        print("")
        return base_stat
