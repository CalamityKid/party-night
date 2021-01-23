from ItemStatusText import (
    intro_text,
    intro_text2,
    intro_text3,
    intro_text4,
    tutorial_text,
    body_check_opener,
    space,
    line,
)
from Format.formatting import (
    format_objects_string,
    format_input,
)
from ItemStatusText import (
    blunt_text,
    Soundcloud_text1,
    Soundcloud_text2,
    G_text1,
    G_text2,
    poppers_text,
    cigarette_text,
    chewing_gum_text,
    lollipop_text,
)
import random

from Setup.PlayerRoomSetup import *  # This is working fine, it calls the instances of rooms and players


class Battle:
    def __repr__(self):
        return "All the battle functions"

    # The active item effect function activates (changes stats) the effect of active items.
    # For an item to become an active item, you call player.use_item function.
    def active_item_effect():  # ALREADY called inside update items so no need to call it. Item effects numbers are here.
        if "Soundcloud" in player.active_items:  # For Soundcloud
            if player.Soundcloud_turn > 0:
                print(Soundcloud_text1)
            if player.Soundcloud_turn == 0:
                print(Soundcloud_text2)
                player.high += 20
                player.lit += 20
                player.mouth -= 20

        if "G" in player.active_items:  # For G
            if player.G_turn > 0:
                print(G_text1)
            if player.G_turn == 0:
                print(G_text2)
                player.high += 10
                player.mouth -= 10
                player.lit += 20

        if "blunt" in player.active_items:  # For blunt
            print(blunt_text)
            player.coolness += 10
            player.high += 10
            player.mouth -= 10
            player.lit += 10

        if "cigarette" in player.active_items:  # For cigarette
            print(cigarette_text)
            player.coolness += 20
            player.lit += 10
            player.high -= 20
            player.mouth -= 10

        if "poppers" in player.active_items:  # For poppers
            print(poppers_text)
            player.high += 10
            player.lit += 100

        if "lollipop" in player.active_items:  # for lollipop
            print(lollipop_text)
            player.mouth += 40
            player.coolness += 10

        if "chewing gum" in player.active_items:  # For chewing gum
            print(chewing_gum_text)
            player.mouth += 30

    # The update items function makes active item effects wane, removes expired items.
    # TO DO !!!!!!!!!! Changed it to being time sensitive.
    def update_items():  # It calls the active item function inside.
        updated_items = {}
        for key, value in player.active_items.items():
            player.active_items[key] = value - 10
            if player.active_items[key] <= 0:
                print("Not feeling the " + key + " anymore.")
                if key == "poppers":
                    player.lit -= 50
            if player.active_items[key] > 0:
                updated_items[key] = player.active_items[key]
        player.active_items = (
            updated_items  # Here we have an updated list after it's over.
        )
        Battle.active_item_effect()
        if player.G_turn is not None and player.G_turn > 0:
            player.G_turn -= 1
        if player.Soundcloud_turn is not None and player.Soundcloud_turn > 0:
            player.Soundcloud_turn -= 1
        player.high -= 5
        player.lit -= 5

    # The body check function evens out maxed or negative stats, and gives the player feedback.
    def body_check():  # should be called AFTER update items.
        body_check_opener()
        if player.high <= 20:  # For high
            print("Pretty sober rn.", end=" ")
        if player.high >= 30 and player.high <= 50:
            print("You can feel the high a bit.", end=" ")
            player.lit += 10
        if player.high >= 60 and player.high <= 70:
            print("This high is feeling goood tho.", end=" ")
            player.lit += 20
        if player.high >= 80 and player.high <= 90:
            print("Great fucking high, the world is yours.", end=" ")
            player.lit += 30
            player.coolness += 10
        if player.high >= 100:
            print("You're waay too high right now, like bad high, you feel... ugh.")
            player.high = 90
            player.coolness -= 10
            player.lit -= 20

        if player.mouth <= 10:  # For mouth
            print("Mouth feels like cardboard, it's really fucking with you.")
            player.coolness -= 10
            player.lit -= 20
            player.mouth = 10
        if player.mouth >= 20 and player.mouth <= 40:
            print("Mouth's getting pretty dry, it's bothering you.")
            player.lit -= 10
        if player.mouth >= 50 and player.mouth < 70:
            print("Mouth's starting to feel a bit dry.")

        if player.lit <= 10:  # For lit
            print("You feel like leaving...", end=" ")
            player.lit = 10
        if player.lit >= 20 and player.lit <= 40:
            print("Not really feeling this party.", end=" ")
        if player.lit >= 50 and player.lit <= 70:
            print("You're enjoying yourself.", end=" ")
        if player.lit >= 80 and player.lit <= 90:
            print("This party's really fucking lit.", end=" ")
        if player.lit >= 100:
            print("You're having the best time of your life.")

        if player.coolness <= 10:  # For coolness
            print("Not getting any attention.")
            player.coolness = 10
        if player.coolness >= 20 and player.coolness <= 40:
            print("Not getting much attention.")
        if player.coolness >= 50 and player.coolness <= 70:
            print("Getting looks from cute people.")
        if player.coolness >= 80 and player.coolness <= 90:
            print("Getting the attention of the hottest people.")
        if player.coolness >= 100:
            print("You're the soul of the party.")
        print("""			""")

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

    def cool_enough(
        interactionee,
    ):  # Checks your coolness against a person's how_cool attr
        if player.coolness >= interactionee.how_cool:
            return True
        else:
            return False

    ##### Identify input for NPCs BELOW ######################
    def identify_person(
        person_to_identify,
    ):  # takes input string, returns a person object, returns None if else

        if "part" in person_to_identify:
            return partner

        elif (
            "smile" in person_to_identify
            or "embass" in person_to_identify
            or "ruben" in person_to_identify
        ):
            return smile

        elif (
            "russ" in person_to_identify
            or "friend" in person_to_identify
            or "misha" in person_to_identify
        ):
            return misha

        elif (
            "cut" in person_to_identify
            or "tank" in person_to_identify
            or "top" in person_to_identify
        ):
            return tanktop

        elif "push" in person_to_identify:
            return pusher

        elif "attrac" in person_to_identify or "couple" in person_to_identify:
            return couple

        elif "beau" in person_to_identify or "breat" in person_to_identify:
            return hottest

        ##### Identify input for NPCs above ######################
        else:
            return None

    #### IDENTIFY INPUT FOR ITEMS HERE
    def identify_item(
        item_to_identify,
    ):  # takes input string, returns an item string, returns None if else

        if "lol" in item_to_identify:
            return "lollipop"

        elif "sound" in item_to_identify or "pill" in item_to_identify:
            return "Soundcloud"

        elif (
            "blunt" in item_to_identify
            or "weed" in item_to_identify
            or "hash" in item_to_identify
        ):
            return "blunt"

        elif (
            item_to_identify == "g"
            or "ghb" in item_to_identify
            or "chorr" in item_to_identify
        ):
            return "G"

        elif "cig" in item_to_identify:
            return "cigarette"

        elif "popp" in item_to_identify:
            return "poppers"

        elif "chew" in item_to_identify:
            return "chewing gum"

        ##### Identify input for items above ######################
        else:
            return None

    # def dance():

    def move():  # The action of moving. This must be set up for every new room in choose_room.
        print("You're currently in " + player.location.name + ".")
        other_rooms_name = []
        for single_room in every_room:
            if single_room != player.location:
                other_rooms_name.append(single_room.name)
        other_rooms_name = format_objects_string(other_rooms_name)
        other_rooms_name = other_rooms_name.replace("and", "or")
        print("You could go to " + other_rooms_name)
        print("You can also [DO] something else.")
        print("")  ##The string of where you can go from here

        def not_there(
            this_room,
        ):  # checks if you're in the room, if you aren't moves you there
            if this_room == player.location:
                print("You're already in " + player.location.name + ".")
                input()
                return False
            elif this_room != player.location:
                player.location = this_room
                print("You make your way to " + player.location.name + ".")
                input()
                Battle.update_room()
                return True

        action = None  ## The input bit
        while action == None:
            print("So where do you wanna go?", end=" ")
            action = input()
            action = format_input(action)  # the input bit

            if action == "do":  # If you wanna do something else
                print("You decide not to move in the end.")
                input()
                Battle.choose_action()

            ################################## Here is where you set each room in move #########
            elif "dance" in action:  # dance floor
                if not_there(dance_floor) == False:
                    action = None

            elif "smok" in action:  # smoking Room
                if not_there(smoking_room) == False:
                    action = None

            elif "bath" in action:  # bathroom
                if not_there(bathroom) == False:
                    action = None

            ############################################################ END room setup ######
            elif "dark" in action:
                print("There's no darkroom in this joint, sorry to say.")
                input()
                action = None

            else:  ####What displays if the room doesn't exist or mispelled.
                input()
                print("Try writing the name of a room.")
                action = None

    def tutorial():  # Tutorial as action in the game
        print(tutorial_text)
        action = None
        while action == None:
            print(
                "Need to [REMEMBER] what you can do or ready to choose an [ACTION]?",
                end=" ",
            )
            action = input()
            action = format_input(action)
            if action == "remember":
                print(space)
                Battle.update_room()

            elif action == "action":
                print(space)
                Battle.choose_action()

            elif action != "remember" and action != "action":
                input()
                print("Read it carefully and try that again.")
                action = None

    def use():  # Use items as action in the game.  ####Set up input for item usage HERE####
        def usable_in_room(usable_item):  # To see if you can use it in this room
            if usable_item in Battle.usable_items_now:
                player.use_item(str(usable_item))
            else:
                print("You shouldn't use that in this room.")

        used_item = None
        action = None  ## The input bit
        while action == None:
            print("What are you gonna go for?", end=" ")
            action = input()
            action = format_input(action)  # the input bit

            if action == "nothing" or action == "no":
                print("You decide not to use anything after all.")
                Battle.choose_action()

            elif action != "nothing":
                used_item = Battle.identify_item(action)
                if used_item != None:
                    usable_in_room(used_item)
                    Battle.update_room()
                    Battle.choose_action()
                elif used_item == None:
                    action = None

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

    def choose_action():  # Prompts the player to the desired action
        def doable_in_room(
            doable_action,
        ):  # To see if you can do an action in this room
            if doable_action in player.location.available_actions:
                return True
            else:
                print("You can't do that in this room.")
                return False

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


def yesorno():
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

    def use_item(
        self, item_used
    ):  ###Used to call battle.update items(), changed it to time sensitive
        if item_used not in self.items:
            print("You don't have that on you.")

            return None
        if item_used in self.items:
            self.active_items[item_used] = total_items[item_used]
            self.items.pop(item_used)
            if "Soundcloud" in item_used:
                self.Soundcloud_turn = 2
            if "G" in item_used:
                self.G_turn = 1
            #######print statements on what item is used
            if (
                item_used == "lollipop"
                or item_used == "cigarette"
                or item_used == "chewing gum"
            ):
                print("You put the " + item_used + " in your mouth.")
            elif item_used == "G" or item_used == "Soundcloud":
                print("You wash down the " + item_used + " with a big gulp.")
            elif item_used == "blunt":
                print("Puff, puff, pass.")
            elif item_used == "poppers":
                print("You huff it all in.")
            ##########


###ITEM SET UP, all the items that exist and how long they last in turns###
### SET UP INPUT words in Battle.identify_items
total_items = {
    "lollipop": 50,
    "Soundcloud": 70,
    "G": 40,
    "blunt": 40,
    "cigarette": 20,
    "poppers": 20,
    "chewing gum": 40,
}
### Item Setup above

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


# Battle.update_room()
# Battle.choose_action()

###########################SCENES

# Create item, action classes and rewrite the functions to accomodate for that
