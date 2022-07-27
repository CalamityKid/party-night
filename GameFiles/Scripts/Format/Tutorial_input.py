# Special input commands used in tutorial


def identify_action_tutorial(action_to_be_identified, dict_of_actions):
    if action_to_be_identified == None:
        return None
    for key, objectx in dict_of_actions.items():
        for identifierx in objectx.identifiers:
            if identifierx in action_to_be_identified:
                return objectx


def identify_object_tutorial(object_to_be_identified_list, player_obj):
    """If passed a list (prior .split() ) and player will check the objects identifiers and return the object"""
    if object_to_be_identified_list == None or object_to_be_identified_list == []:
        return None
    for word in object_to_be_identified_list:
        for key, objectx in player_obj.dict_of_objects.items():
            for identifierx in objectx.identifiers:
                if identifierx in word:
                    return objectx


def identify_object_check_tutorial(object_to_be_identified_list, player_obj):
    """Modified identify_object for Check action, also returns actions and other stuff. modify object: If passed a list (prior .split() ) and player.dict_of:objects will check the objects identifiers and return the object"""
    if object_to_be_identified_list == None:
        return None
    for word in object_to_be_identified_list:
        for key, objectx in player_obj.dict_of_objects.items():
            for identifierx in objectx.identifiers:
                if identifierx in word:
                    return objectx
                if word == "time":
                    return player_obj.time
                if word == "party" or word == "mood":
                    return player_obj.party
                if (
                    word == "body"
                    or word == "feeling"
                    or word == "feelings"
                    or word == "myself"
                ):
                    return player_obj
                if word == "action" or word == "actions":
                    return "actions check"
                if word == "pockets" or word == "items" or word == "holding":
                    return "item check"
                if word == "around" or word == "room":
                    return player_obj.location
                if word == "party":
                    return player_obj.party
                if word == "friends":
                    return "friends"


def clean_input(to_clean):
    result = None
    if type(to_clean) == str:
        result = to_clean.lower()
        result = result.strip()
        return result
    elif type(to_clean) != str:
        return None


def format_input_command_tutorial(player_input, player_obj):
    action = None
    subject = None
    player_input = clean_input(player_input)
    player_input = player_input.split()
    if len(player_input) == 0:
        return None, None

    elif len(player_input) >= 1:
        action = player_input[0]
        action = identify_action_tutorial(action, player_obj.dict_of_actions)

    if len(player_input) >= 2:
        subject = player_input[1:]

    if "Check" in player_obj.dict_of_actions:
        if action == player_obj.dict_of_actions["Check"]:
            subject = identify_object_check_tutorial(subject, player_obj)

        elif (
            hasattr(action, "name") == True and "Check" not in action.name
        ) or hasattr(action, "name") == False:
            subject = identify_object_tutorial(subject, player_obj)
    else:
        subject = identify_object_tutorial(subject, player_obj)

    if "Dance" in player_obj.dict_of_actions:
        if subject == None and (action == player_obj.dict_of_actions["Dance"]):
            subject = True
    elif "Tap Water" in player_obj.dict_of_actions:
        if subject == None and (action == player_obj.dict_of_actions["Tap Water"]):
            subject = True

    return action, subject


def player_choose_action_tutorial(player_obj):
    """Returns (action, object) if identified in the temporary list in tutorial; [object can be object with .name or can be True or a string]"""
    action_met = None
    while action_met == None:
        inputaction = None
        inputobject = None
        while (inputaction == None) or (inputobject == None):
            currentinput = input("Try typing a command: ")
            inputaction, inputobject = format_input_command_tutorial(
                currentinput, player_obj
            )
            if inputaction == None or inputobject == None:
                print("Try typing that again.")
                # print("Try again, bitch. One of the things is None. It won't execute.")
                inputaction = None
                inputobject = None

        print("")
        action_met = True
        return inputaction, inputobject


def yesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = clean_input(yesornoresult)
            if "y" in yesornoresult[0]:
                print("")
                return True
            elif "n" in yesornoresult[0]:
                print("")
                return False
        print("(yes or no): ", end=" ")
        yesornoresult = None
