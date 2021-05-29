
class Battle:
    def __repr__(self):
        return "All the battle functions"

    # TO DO !!!!!!!!!! Changed it to being time sensitive.
    def update_room():  # Updates people in this room, informs where you are and what you can do. Calls choose_action in the end.
        people_in_this_room = []
        people_in_room_string = ""
        usable_items_now = []
        usable_items_now_string = ""
        available_actions_string = ""

        for person in every_NPC:  # Updates Battle.people_in_this_room
            if person.location == player.location:
                people_in_this_room.append(person)
        Battle.people_in_this_room = people_in_this_room
        people_in_room_string = format_objects_string(people_in_this_room)
        if people_in_room_string == "nothing":
            people_in_room_string = "no familiar faces."

        for key, value in player.items.items():  # Updates Battle.usable_items_now
            if key in player.location.usable_items:
                usable_items_now.append(key)
        Battle.usable_items_now = usable_items_now
        usable_items_now_string = format_objects_string(usable_items_now)

        available_actions_string = format_objects_string(
            player.location.available_actions
        )  # formats actions available

        print("You're currently in the " + player.location.name + ".", end=" ")
        print("You can see " + people_in_room_string)
        if people_in_room_string != "no familiar faces.":
            print("You could [TALK] to them.")
        if len(usable_items_now) == 0:
            print("You don't have anything you can [USE] in this room.")
        elif len(usable_items_now) > 0:
            print(
                "In this room, you could probably safely [USE] your "
                + usable_items_now_string
            )
        available_actions_string = available_actions_string.replace("and", "or")
        print("You could also " + available_actions_string)
        Battle.choose_action()


            if action == "do":  # If you wanna do something else
                print("You decide not to move in the end.")
                input()
                Battle.choose_action()



    def tap_water():  # drink tap water as an action
        print("It's definitely not your best look, but free water is free water.")
        player.coolness -= 10
        player.mouth += 40
        Battle.choose_action()

    def borrow():  # borrow an item from a person
        def in_this_room(
            borrowee,
        ):  # takes a person object returns True if in current room
            if borrowee in Battle.people_in_this_room:
                return True
            else:
                print("They aren't in this room.")
                return False

        action = None  # takes input to select person to borrow from
        person = None
        while action == None:
            print("Who do you want to borrow from?", end=" ")
            action = input()
            action = format_input(action)

            if (
                action == "no"
                or action == "nobody"
                or action == "no one"
                or action == "noone"
            ):
                print("You change your mind.")
                Battle.choose_action()
                break
            person = Battle.identify_person(action)
            if person == None:
                action = None

            elif in_this_room(person) == False:
                action = None

            elif (
                Battle.cool_enough(person) == False
            ):  # checks if youre cool enough to borrow from them
                print("You can't summon the confidence to ask them for anything.")
                action = None

            elif Battle.cool_enough(person) == True:  # string with what they have
                if format_objects_string(person.items) == "nothing":
                    print("They have nothing else for you to borrow.")
                    Battle.choose_action()
                    break
                print(
                    "They have "
                    + (format_objects_string(person.items)[:-1])
                    + " on them."
                )

                item_borrowed = None  ## Second input to select item
                while item_borrowed == None:
                    print("What will you borrow?", end=" ")
                    item_borrowed = input()
                    item_borrowed = format_input(item_borrowed)

                    if item_borrowed == "nothing" or action == "no":
                        print(
                            "You change your mind and politely decide not to borrow anything."
                        )
                        Battle.choose_action()
                        break

                    item_borrowed = Battle.identify_item(item_borrowed)

                    if item_borrowed not in person.items:
                        print("They don't have any of that.")
                        item_borrowed = None

                    elif item_borrowed in player.items:
                        print("You already have some of that.")
                        item_borrowed = None

                    elif item_borrowed in person.items:
                        print("They give you their " + item_borrowed + ".")
                        player.items[item_borrowed] = total_items[item_borrowed]
                        person.items.remove(item_borrowed)
                        Battle.choose_action()
                        break



        action = None
        while action == None:
            print("What do you want to do?", end=" ")
            action = input()
            action = format_input(action)

            input()  # For space and pause
            if "tuto" in action:
                Battle.tutorial()

            elif action == "move":
                Battle.move()

            elif action == "use":
                Battle.use()

            elif action == "tap":
                if doable_in_room("drink [TAP] water") == True:
                    Battle.tap_water()
                else:
                    action = None

            elif action == "check":
                Battle.update_room()

            elif action == "borrow":
                Battle.borrow()

            elif action == "pass":
                Time.ten_minutes()
                action = None

            elif action == "time":
                print(time)
                action = None

            else:
                action = None

            # elif:
            # 	action == "dance":
            # 	Battle.dance()





party = Party("empty", "okay")
scenevariables = SceneVariables()

##TO DO Borrow cigarette,
## NOTE that player items are a dictionary while user items are a LIST.

total_available_actions = [
    "[FLIRT]",
    "[DANCE]",
    "[TALK]",
    "[BORROW] something",
    "drink [TAP] water",
    "[MOVE] to another room",
    "[LEAVE] the party",
    "lollipop",
    "Soundcloud",
    "G",
    "blunt",
    "cigarette",
    "poppers",
    "chewing gum",
]
time = Time(1, 30)
###########################SCENES

