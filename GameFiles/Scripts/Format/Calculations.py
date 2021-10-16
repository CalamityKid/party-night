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


def calculate_goods(object):
    """takes an object's lit and high attr and averages it"""
    return int((object.lit + object.high) / 2)


def calculate_bads(object):
    """returns an object's (coolness - friend boost). Only use with instance, not with player"""
    return int(object.coolness - object.friend_boost)


def assign_bool(var, intvalue=50):
    """Auxiliary function for narrate goods in Dance narration.
    Takes a variable, if less than 50 returns true or false"""
    if var > intvalue:
        print(True)
        return True
    elif var <= intvalue:
        print(False)
        return False
    else:
        raise ValueError(
            "assign bool inside narrate goods inside dance narration, result is", var
        )


def create_bool_dict(dance_instance):
    """Auxiliary function that returns a bool dict to use in narrations given a dance instance"""
    final_dict = {}

    ## Assign booleans in order to create narrations
    final_dict["result"] = assign_bool(dance_instance.result)
    final_dict["lit"] = assign_bool(dance_instance.lit)
    final_dict["high"] = assign_bool(dance_instance.high)

    final_dict["concuerda"] = final_dict["lit"] == final_dict["high"]
    return final_dict


def TorF(var):
    """auxiliary function, returns string T or F if given Bool"""
    assert type(var) == bool
    if var == True:
        return "T"
    else:
        return "F"


def create_goods_code(bool_dict):
    """takes the bool dict and returns a list of codes to build goods sentence narration"""
    assert "result" in bool_dict
    list_result = []
    prefix = "r"
    prefix += TorF(bool_dict["result"])

    for i in ["lit", "high"]:
        stringi = prefix
        stringi += i[0]
        stringi += TorF(bool_dict[i])
        print(stringi)
        list_result.append(stringi)

    return list_result
