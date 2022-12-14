from time import sleep
from .Scripts.Format import formatting


def player_choose_action(player_obj):
    executed = None
    counter = 0
    while executed != True:
        inputaction = None
        inputobject = None
        while (inputaction == None) or (inputobject == None):
            currentinput = input("What do you want to do? ")
            inputaction, inputobject = formatting.format_input_command(
                currentinput, player_obj
            )
            if inputaction == None or inputobject == None:
                # print("One of the things is None. It won't execute.")
                inputaction = None
                inputobject = None
                print("")
                print("that wasn't very clear... can you try that again?")
                sleep(1)
                counter += 1
                if counter > 2:
                    print(
                        "You can type TUTORIAL if you're having problems with commands."
                    )
        ######################################### tap water exception
        if (
            inputaction == player_obj.dict_of_actions["Use"]
            and inputobject == player_obj.dict_of_actions["Tap Water"]
        ):
            inputaction = player_obj.dict_of_actions["Tap Water"]
            inputobject = True

        print("")
        action_met = inputaction.execute(player_obj, inputobject)
        executed = True
        print("")
        return action_met

        # if action_met == None:    #this is if execute returns none
        # print("execute returned None. So time doesn't pass. Try something else.")


def yesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = formatting.clean_input(yesornoresult)
            if (
                "y" in yesornoresult[0]
                or yesornoresult == "ok"
                or yesornoresult == "okay"
            ):
                print("")
                return True
            elif "n" in yesornoresult[0]:
                print("")
                return False
        print("(yes or no): ", end=" ")
        yesornoresult = None
