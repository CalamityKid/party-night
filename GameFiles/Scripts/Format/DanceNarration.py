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


def assign_bool(var, intvalue=50):
    """Auxiliary function for narrate goods in Dance narration.
    Takes a variable, if less than 50 returns true or false"""
    print("int value is ", intvalue, "assign bool for", var, end=": ")
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


def narrate_goods(dance_instance):
    """Given a dance instance, builds a sentence narrating lit and high"""
    str_list = []
    concuerda = None
    resultBool = None
    litBool = None
    highBool = None

    ## Assign booleans in order to create narrations
    resultBool = assign_bool(dance_instance.result)
    litBool = assign_bool(dance_instance.lit)
    highBool = assign_bool(dance_instance.high)

    concuerda = litBool == highBool

    # Actual narration
    print("concuerda is ", concuerda)


str1 = "hi. "
str2 = "Whats going on in here dawg?"
strlist = []
strlist.append(str1)
strlist.append("Whats going on in here dawg?")
list_as_string = "".join(strlist)
print(list_as_string)
print(strlist)
