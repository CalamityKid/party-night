narrate_lit_dict = {
    "rTlT": "You're having a great time tonight",
    "rTlF": "You're aren't enjoying yourself right now",
    "rFlT": "You're enjoying yourself tonight",
    "rFlF": "You're not really feeling this party right now",
}
narrate_high_dict = {
    "rThT": "you're really feeling this high... ",
    "rThT": "even though you're pretty sober... ",
    "rFhT": "even though you're pretty high... ",
    "rFhF": "you're definitely too sober for this... ",
}
narrate_conjunction_dict = {True: " and ", False: " but "}
narrate_result_ending_dict = {
    True: "you really get into the music.",
    False: "you can't really get lost in the music.",
}


def dance_flourish():
    print("****")
    print(" **")
    print("   *")
    return None


def narrate_goods(dance_instance):
    """Given a dance instance, builds a sentence narrating lit and high"""
    str_list = []
    list_as_string = ""

    bool_dict = dance_instance.bool_dict
    goods_code = dance_instance.goods_code

    # builds the sentence
    str_list.append(narrate_lit_dict[goods_code[0]])
    str_list.append(narrate_conjunction_dict[bool_dict["concuerda"]])
    str_list.append(narrate_high_dict[goods_code[1]])
    str_list.append(narrate_result_ending_dict[bool_dict["result"]])

    # joins it together and returns it
    list_as_string = "".join(str_list)
    return list_as_string
