modified_cause_dict = {"lit": "mod_lit", "high": "mod_high", "cool": "mod_cool"}

def narrate_result(player, result):
    dance_flourish()
    if result <= 40: #bad result
        print ("Bad result this time")

        pass
    
    elif result > 40 and result <70: #ok result
        pass

    elif result >= 70 and result <100: #great results
        pass

    elif result >= 100: 
        pass


def dance_flourish():
    print ("****")
    print (" **")
    print ("   *")
    return None


def identify_causes(player, good_or_bad):
    causes = []
    if good_or_bad == True:
        for attr in ["lit", "high"]:
            if getattr(player,attr) <= 40:
                causes.append(attr)
        if player.coolness => 50:
            causes.append("coolness")
            return causes
    elif good_or_bad == False:
        for attr in ["lit", "high"]:
            if getattr(player,attr) >= 40:
                causes.append(attr)
        if player.coolness <= 50:
            causes.append("coolness")
            return causes


#checks if theres a 30 point dif between a player stat and a modded stat
def mod_helped (player, dance_instance, good_or_bad): 
    result = {}
    if good_or_bad == True:
        for key, value in modified_cause_dict.items():
            if dance_instance.value - player.key > 30:
                result[key] = True
    
    elif good_or_bad == False:
        for key, value in modified_cause_dict.items():
            if player.key - dance_instance.value > 30:
                result[key] = True
    
    return result
