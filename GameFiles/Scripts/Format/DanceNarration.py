from random import randint
from time import sleep
from .Narration import people_in_room_string
from ...Sound.Sounds import play_tap, play_toop, play_in, play_out


# Narrate goods
narrate_lit_dict = {
    "rTlT": "You're having a great time tonight",
    "rTlF": "You're aren't enjoying yourself right now",
    "rFlT": "You're enjoying yourself tonight",
    "rFlF": "You're not really feeling this party right now",
}
narrate_high_dict = {
    "rThT": "you're really feeling this high... ",
    "rThF": "even though you're pretty sober... ",
    "rFhT": "even though you're pretty high... ",
    "rFhF": "you're definitely too sober for this... ",
}
narrate_conjunction_dict = {True: " and ", False: " but "}
narrate_result_ending_dict = {
    True: "you really get into it.",
    False: "you can't really get into it.",
}
######Narrate bads
narrate_cool_dict = {
    1: "You start feeling self conscious",
    2: "Lots of cuties around, you start feeling anxious",
}
cool_conjunction = {True: ", but ", False: " and "}
narrate_friend_boost_dict = {
    "rTf1": "You start dancing with your partner and start getting into it.",
    "rTf2": "You see your friends around and start getting into the groove.",
    "rTf3": "You see all your friends having a great time and you start to feel the music.",
    "rFf1": "You wish your friends were also here dancing with you.",
    "rFf2": "You start dancing with your friends and just can't get into it.",
    "rFf3": "Even with all your friends here you can't get into it.",
}
# intro
flourish = {0: ["***", "**", "*"], 1: ["*", "**", "***"]}
flourish_sound = {
    0: [play_tap, play_tap, play_toop],
    1: [play_toop, play_toop, play_tap],
}
dance_bark_dict = {
    0: "The music's sounding {music} now. ",
    1: "The beats are {music} atm. ",
}

# outcomes
outcomes_intro_str = "The dancing's {outcome}. "
outcomes_dict = {
    1: "You end up feeling kinda dumb.",
    2: "You kinda just move to the music.",
    3: "You enjoy yourself. It was cool.",
    4: "You really enjoy yourself. It's a blast.",
    5: "You dance up a storm and feel like a star. You get compliments from people.",
}


def dance_flourish(dance_instance):
    """prints flourish. if counter is odd starts ***, if even starts *"""
    flourish_bool = dance_instance.flourish_counter % 2
    soundi = 0
    sound_list = flourish_sound[flourish_bool]
    for i in flourish[(flourish_bool)]:
        print(i)
        sound_list[soundi]()
        soundi += 1
        sleep(1)
    dance_instance.flourish_counter += 1


def dance_bark(player_object):
    op = randint(0, (len(dance_bark_dict) - 1))
    print(dance_bark_dict[op].format(music=player_object.party.music))
    play_in()
    sleep(1)


def narrate_opening(player_object, ppl_in_room):
    """given player object and list of people in room,
    returns an opening describing the music"""
    string_list = []
    list_as_string = ""
    ppl_in_room_str = people_in_room_string(player_object)
    dance_bark(player_object)

    if len(ppl_in_room_str) > 13:
        string_list.append("Dancing around you see ")
        string_list.append(ppl_in_room_str)
    else:
        string_list.append("Your friends aren't around.")
    list_as_string = "".join(string_list)
    return list_as_string


def narrate_goods(dance_instance):
    """Given a dance instance, builds a sentence narrating lit and high"""
    str_list = []
    list_as_string = ""

    bool_dict = dance_instance.bool_dict
    goods_code = dance_instance.goods_code

    # builds the sentence
    str_list.append(narrate_lit_dict[goods_code["lit code"]])
    str_list.append(narrate_conjunction_dict[bool_dict["concuerda"]])
    str_list.append(narrate_high_dict[goods_code["high code"]])
    str_list.append(narrate_result_ending_dict[bool_dict["result"]])

    # joins it together and returns it
    list_as_string = "".join(str_list)
    return list_as_string


def narrate_bads(dance_instance):
    """Given a dance instance, builds a sentence with cool and friend boost"""
    str_list = [""]
    list_as_string = ""
    bads_code = dance_instance.bads_code

    if "cool phrase" in bads_code:
        str_list = []
        str_list.append(narrate_cool_dict[bads_code["cool phrase"]])
        str_list.append(cool_conjunction[bads_code["cool conjunction"]])
        str_list.append(narrate_friend_boost_dict[bads_code["friend code"]].lower())

    else:
        str_list.append(narrate_friend_boost_dict[bads_code["friend code"]])

    list_as_string = "".join(str_list)
    return list_as_string


def narrate_outcomes(number, string):
    """given the outcome tuple, returns a final string narrating outcomes"""
    str_list = [outcomes_intro_str.format(outcome=string)]
    list_as_string = ""
    str_list.append(outcomes_dict[number])
    list_as_string = "".join(str_list)
    return list_as_string
