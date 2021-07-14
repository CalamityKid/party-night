modified_cause_dict = {"lit": "mod_lit", "high": "mod_high", "coolness": "mod_coolness"}


def narrate_result(player, result):
    dance_flourish()
    if result <= 40:  # bad result
        print("Bad result this time")

        pass

    elif result > 40 and result < 70:  # ok result
        pass

    elif result >= 70 and result < 100:  # great results
        pass

    elif result >= 100:
        pass


def dance_flourish():
    print("****")
    print(" **")
    print("   *")
    return None


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
