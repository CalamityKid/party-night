from .Scripts.Format import formatting


def player_choose_action(player_obj):
    action_met = None
    while action_met == None:
        inputaction = None
        inputobject = None
        while (inputaction == None) or (inputobject == None):
            currentinput = input("What do you want to do? ")
            inputaction, inputobject = formatting.format_input_command(
                currentinput, player_obj
            )
            if inputaction == None or inputobject == None:
                print(inputaction, inputobject)
                print("What?")
                # print("Try again, bitch. One of the things is None. It won't execute.")
                inputaction = None
                inputobject = None
        ######################################### tap water exception
        if (
            inputaction == player_obj.dict_of_actions["Use"]
            and inputobject == player_obj.dict_of_actions["Tap Water"]
        ):
            inputaction = player_obj.dict_of_actions["Tap Water"]
            inputobject = True
        # print("executing!")

        print("")
        action_met = inputaction.execute(player_obj, inputobject)
        print("")
        # if action_met == None:    #this is if execute returns none, maybe add a counter here
        # print("execute returned None. So time doesn't pass. Try something else:, maybe here refresh available actions, also maybe a counter")


def yesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = formatting.clean_input(yesornoresult)
            if "y" in yesornoresult[0]:
                print("")
                return True
            elif "n" in yesornoresult[0]:
                print("")
                return False
        print("(yes or no): ", end=" ")
        yesornoresult = None
