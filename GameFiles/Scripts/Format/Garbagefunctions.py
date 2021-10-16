def identify_causes(player, good_or_bad):
    causes = []
    if good_or_bad == False:
        for attr in ["lit", "high"]:
            if getattr(player, attr) <= 30:
                causes.append(attr)
        if player.coolness >= 60:
            causes.append("coolness")

    elif good_or_bad == True:
        for attr in ["lit", "high"]:
            if getattr(player, attr) >= 50:
                causes.append(attr)
        if player.coolness <= 30:
            causes.append("coolness")
    print(good_or_bad, "causes are", causes)
    return causes


# checks if theres a 30 point dif between a player stat and a modded stat
modified_cause_dict = {"lit": "mod_lit", "high": "mod_high", "coolness": "mod_coolness"}
def mod_helped(player, dance_instance, good_or_bad):
    result = []
    print("mod:", good_or_bad)
    for key, value in modified_cause_dict.items():
        instance_value = getattr(dance_instance, value)
        player_value = getattr(player, key)
        print(key, value)
        print(player_value, instance_value)

        if good_or_bad == True:
            if instance_value - player_value > 30:
                result.append(key)

        elif good_or_bad == False:
            if player_value - instance_value > 30:
                result.append(key)

    print("mod results are", result)
    return result


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