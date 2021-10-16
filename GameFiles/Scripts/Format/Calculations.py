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
    totaladded = 0
    count = 0
    grandtotal = 0
    base_stat = getattr(player, variable_in_string)
    for item, effect in player.active_items.items():
        print(item, ":")
        if hasattr(item, mod_name) == True:
            totaladded += (base_stat * ((getattr(item, mod_name)))) - base_stat
            count += 1
    grandtotal = int(base_stat + totaladded)
    if grandtotal > 100:
        grandtotal = 100
    if count > 0:
        print(
            variable_in_string,
            "base is",
            base_stat,
            "the mod is returning",
            grandtotal,
        )
        print("")
        return grandtotal
    elif count == 0:
        print(variable_in_string, "isnt modded, returns", base_stat)
        print("")
        return int(base_stat)


def outcome(number_to_calculate):
    """takes an int (result of dance calc) from -50 to 100 and returns a tuple"""
    if (
        type(number_to_calculate) != int
        or number_to_calculate < -100
        or number_to_calculate > 200
    ):
        raise ValueError(
            "outcome function in Calculations.py, argument should be an int (-100 -- 200) and is instead",
            number_to_calculate,
        )
    elif number_to_calculate <= 30:
        return (1, "bad")
    elif number_to_calculate <= 50:
        return (2, "ok")
    elif number_to_calculate <= 70:
        return (3, "good")
    elif number_to_calculate <= 100:
        return (4, "great")
    elif number_to_calculate > 100:
        return (5, "amazing")


def calculate_goods(object):
    """takes an object's lit and high attr and averages it"""
    return int((object.lit + object.high) / 2)


def calculate_bads(object):
    """returns an object's (coolness - friend boost). Only use with instance, not with player"""
    return int(object.coolness - object.friend_boost)
