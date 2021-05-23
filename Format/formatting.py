def identify_object(object_to_be_identified_list, dict_of_objects):
    if object_to_be_identified_list == None:
        return None
    for word in object_to_be_identified_list:
        for key, objectx in dict_of_objects.items():
            for identifierx in objectx.identifiers:
                if identifierx in word:
                    return objectx


def identify_action(action_to_be_identified, dict_of_actions):
    if action_to_be_identified == None:
        return None
    for key, objectx in dict_of_actions.items():
        for identifierx in objectx.identifiers:
            if identifierx in action_to_be_identified:
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


def format_input_command(player_input, dict_of_actions, dict_of_objects):
    action = None
    subject = None
    player_input = clean_input(player_input)
    player_input = player_input.split()
    try:
        action = player_input[0]
        subject = player_input[1:]
    except IndexError:
        action = None
        subject = None
    #####################################################################
    action = identify_action(action, dict_of_actions)
    if action == None:
        return None
    #######################################################################
    subject = identify_object(subject, dict_of_objects)
    if subject == None:
        return None
    print(action, subject)
    return action, subject


# You feed it a list and it gives you a string. pretty sure i can make it take an attribute if I rewrite it with getattr


def format_objects_string(
    given_list,
):  # Returns "nothing" if empty list, returns "object, object, and object." style string.
    final_string = ""

    if len(given_list) == 0:
        return "nothing"

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


def inputyesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = yesornoresult.lower()
            if "y" in yesornoresult[0]:
                return True
            elif "n" in yesornoresult[0]:
                return False
        print("(yes or no):", end=" ")
        yesornoresult = None
