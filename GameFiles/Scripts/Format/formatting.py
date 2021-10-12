from ..Blocks.PlayerSc import player
from ..Blocks.ItemsSc import items
from ..Blocks.TimeSc import time
from ..Blocks.PartySc import party


def identify_object(object_to_be_identified_list, dict_of_objects):
    if object_to_be_identified_list == None or object_to_be_identified_list == []:
        return None
    for word in object_to_be_identified_list:
        for key, objectx in dict_of_objects.items():
            for identifierx in objectx.identifiers:
                if identifierx in word:
                    return objectx
                # exception for G
                if word == "g":
                    # print("identify object: G exception")
                    return items["G"]
                if word == "tap" or word == "water":
                    # print("identify object: tap exception")
                    return player.dict_of_actions["Tap Water"]
    # print("Identify object i guess returns None cause nothing was identified")


def identify_object_check(object_to_be_identified_list, dict_of_objects):
    if object_to_be_identified_list == None:
        return None
    for word in object_to_be_identified_list:
        for key, objectx in dict_of_objects.items():
            for identifierx in objectx.identifiers:
                if identifierx in word:
                    return objectx
                # exception for G
                if word == "g":
                    return items["G"]
                if word == "tap" or word == "water":
                    return player.dict_of_actions["Tap Water"]
                if word == "time":
                    return time
                if word == "party" or word == "mood":
                    return party
                if (
                    word == "body"
                    or word == "feeling"
                    or word == "feelings"
                    or word == "myself"
                ):
                    return player
                if word == "action" or word == "actions":
                    return "actions check"
                if word == "pockets" or word == "items" or word == "holding":
                    return "item check"
                if word == "around" or word == "room":
                    return player.location
                if word == "party":
                    return party
                if word == "friends":
                    return "friends"


def identify_action(action_to_be_identified, dict_of_actions):
    if action_to_be_identified == None:
        return None
    for key, objectx in dict_of_actions.items():
        for identifierx in objectx.identifiers:
            if identifierx in action_to_be_identified:
                print("identified action:")
                print(objectx)
                return objectx


def clean_input(to_clean):
    result = None
    if type(to_clean) == str:
        result = to_clean.lower()
        result = result.strip()
        return result
    elif type(to_clean) != str:
        print("clean_input wasn't fed a string.")
        return None


def format_input_command(player_input):
    action = None
    subject = None
    player_input = clean_input(player_input)
    player_input = player_input.split()
    if len(player_input) == 0:
        return None, None

    elif len(player_input) >= 1:
        action = player_input[0]
        action = identify_action(action, player.dict_of_actions)

    if len(player_input) >= 2:
        subject = player_input[1:]

        if action == player.dict_of_actions["Check"]:
            subject = identify_object_check(subject, player.dict_of_objects)

        elif action != player.dict_of_actions["Check"]:
            subject = identify_object(subject, player.dict_of_objects)

    if subject == None and (
        action == player.dict_of_actions["Tap Water"]
        or action == player.dict_of_actions["Dance"]
    ):
        subject = True

    return action, subject


def format_objects_string(
    given_list,
):  # Returns "nothing" if empty list, returns "object, object, and object." style string.
    final_string = ""
    try:
        if len(given_list) == 0:
            return "nothing"
    except TypeError:
        pass

    try:
        if hasattr(given_list[0], "name") == True:  # If it's a list of objects
            if len(given_list) == 1:
                return given_list[0].name + "."
            if len(given_list) == 2:
                return given_list[0].name + " and " + given_list[1].name + "."
            if len(given_list) >= 3:
                for item in given_list[:-2]:
                    final_string += item.name + ", "
                final_string += (
                    given_list[-2].name + " and " + given_list[-1].name + "."
                )
            return final_string
    except KeyError:
        pass
    if (type(given_list)) == dict:  # If it's a dictionary
        listed_dic = []
        for key, value in given_list.items():
            listed_dic.append(key)
        if len(listed_dic) == 1:
            return listed_dic[0] + "."
        if len(listed_dic) == 2:
            return listed_dic[0] + " and " + listed_dic[1] + "."
        if len(listed_dic) >= 3:
            for item in listed_dic[:-2]:
                final_string += item + ", "
            final_string += listed_dic[-2] + " and " + listed_dic[-1] + "."
        return final_string

    if (type(given_list)) == list:  # If it's a list
        if len(given_list) == 1:
            return given_list[0] + "."
        if len(given_list) == 2:
            return given_list[0] + " and " + given_list[1] + "."
        if len(given_list) >= 3:
            for item in given_list[:-2]:
                final_string += item + ", "
            final_string += given_list[-2] + " and " + given_list[-1] + "."

        return final_string
