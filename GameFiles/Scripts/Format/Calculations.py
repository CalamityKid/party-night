# from GameFiles.Scripts.Format.Garbagefunctions import outcome


def create_list_people_in_room(player):
    """ "given player object, returns a list of objects of people in that room"""
    people_in_room_list = []
    for person in player.people_in_party:
        if person.location == player.location:
            people_in_room_list.append(person)
    return people_in_room_list


def calculate_friend_boost(ppl_room_list, debug=False):
    """Given a list of people in room, returns the total boost in full int (mult of 10)
    used in dance calculations"""
    total_boost = 0
    for person in ppl_room_list:
        total_boost += person.boost
    if debug == True:
        print("total boost is", total_boost)
    return int(total_boost * 10)


def calculate_mod_item_effect(player, variable_in_string, debug=False):
    mod_name = str(variable_in_string) + ("_mod")
    totaladded = 0
    count = 0
    grandtotal = 0
    base_stat = getattr(player, variable_in_string)
    for item, effect in player.active_items.items():
        if debug == True:
            print(item, ":")
        if hasattr(item, mod_name) == True:
            totaladded += (base_stat * ((getattr(item, mod_name)))) - base_stat
            count += 1
    grandtotal = int(base_stat + totaladded)
    if grandtotal > 100:
        grandtotal = 100
    if count > 0:
        if debug == True:
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
        if debug == True:
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
        return True
    elif var <= intvalue:
        return False
    else:
        raise ValueError(
            "assign bool inside narrate goods inside dance narration, result is", var
        )


def create_bool_dict(dance_instance):
    """Auxiliary function that returns a bool dict to use in narrations given a dance instance
    the keys are "result", "lit", "high" """
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
    """takes the bool dict and returns a dict with "lit code" and "high code" """
    assert "result" in bool_dict
    code_dict = {}
    code_prefix = "r"
    code_prefix += TorF(bool_dict["result"])
    code_suffix = " code"

    for i in ["lit", "high"]:
        code_name = i
        code_name += code_suffix
        code = code_prefix
        code += i[0]
        code += TorF(bool_dict[i])

        code_dict[code_name] = code

    return code_dict


def create_bads_code(dance_instance):
    """takes dance instance, returns bads code dict
    returns dict with {"friend code": rFf#, "cool conjunction": boolean depending on result, may include "cool phrase": 1 2 or not at all}"""
    code_dict = {}
    boost = dance_instance.friend_boost
    assert type(boost) == int

    resultbool = dance_instance.bool_dict["result"]
    code_dict["cool conjunction"] = resultbool

    fc = "r"
    fc += TorF(resultbool)
    fc += "f"
    if boost < 20:
        fc += "1"
    elif boost >= 20 and boost <= 30:
        fc += "2"
    elif boost > 30:
        fc += "3"

    code_dict["friend code"] = fc

    # cool phrase and if sentence is passed or not
    if dance_instance.coolness >= 40 and dance_instance.coolness < 70:
        code_dict["cool phrase"] = 1

    elif dance_instance.coolness >= 70:
        code_dict["cool phrase"] = 2

    return code_dict


def calculate_outcome(number_to_calculate):
    """takes an int (result of dance calc) and returns an outcome tuple, number and string
    to be used in other narration functions"""
    assert type(number_to_calculate) == int
    if number_to_calculate <= 30:
        return (1, "bad")
    elif number_to_calculate <= 50:
        return (2, "ok")
    elif number_to_calculate <= 70:
        return (3, "good")
    elif number_to_calculate <= 100:
        return (4, "great")
    elif number_to_calculate > 100:
        return (5, "amazing")


def outcome_on_stats(player_object, outcome_number, outcome_bool):
    """given player, outcome number and outcome bool, runs player.modify stat
    to alter stats + or - based on the result"""
    to_be_modified = int(outcome_number * 10)
    for i in ["lit", "coolness"]:
        player_object.modify_stat(i, to_be_modified, outcome_bool)


def not_on_dance_floor(player):
    """given player, checks if the chars are on dance floor for the change music scene"""
    final_list = []
    chars_to_check = [
        player.NPCs["couple"],
        player.NPCs["russian"],
        player.NPCs["smile"],
    ]
    for person in chars_to_check:
        if person.location != player.rooms["dance floor"]:
            final_list.append(person)
    return final_list
