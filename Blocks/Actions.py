from Blocks.Room import Room
from Blocks.Items import Item
from Blocks.PlayerNPC import MainCharacter, NPC


class Action:
    def __init__(
        self,
        name,
        identifiers,
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers
        # self.object_performing_the_action = object_performing_the_action
        # self.object_to_be_interacted_with = object_to_be_interacted_with
        # Maybe these arent necesary actually
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def __repr__(self):
        return str(self.name)


class Move(Action):
    def __init__(
        self,
        name="Move to",
        identifiers=["move", "go"],
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers

    def execute(self, object_performing_the_action, object_to_be_interacted_with):

        if object_performing_the_action.location == object_to_be_interacted_with:
            print("You're already in this room.")
            return None
        elif object_performing_the_action.location != object_to_be_interacted_with:
            if isinstance(object_to_be_interacted_with, Room) == True:
                object_performing_the_action.location = object_to_be_interacted_with
                print(
                    object_performing_the_action.name,
                    "moves to",
                    object_to_be_interacted_with.name + ".",
                )
            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("You can't move to " + object_to_be_interacted_with.name + ".")
                print("You can only move to other rooms.")
                return None


class Use_Item(Action):
    def __init__(
        self,
        name="Use",
        identifiers=["use", "item", "smoke", "take", "do"],
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        if isinstance(object_to_be_interacted_with, Item) != True:
            print("You can't use", object_to_be_interacted_with.name, ".")
            if isinstance(object_to_be_interacted_with, MainCharacter) == True:
                print("I mean, not in that way anyway.")
            print("You can only use the things you're holding.")
            return None
        if object_to_be_interacted_with not in object_performing_the_action.items:
            print("You don't have that on you.")
            return None
        elif object_to_be_interacted_with in object_performing_the_action.items:
            if (
                object_to_be_interacted_with
                in object_performing_the_action.active_items
            ):
                print("You've had that recently.")
                return None
            elif (
                object_to_be_interacted_with
                not in object_performing_the_action.active_items
            ):
                object_performing_the_action.items.remove(object_to_be_interacted_with)
                print(object_to_be_interacted_with.use_text)
                object_performing_the_action.active_items[
                    object_to_be_interacted_with
                ] = object_to_be_interacted_with.duration
            # x = object_performing_the_action.items.pop(
            # object_to_be_interacted_with.name)

            # also remember to check if it has a delay


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

move = Move()
use_item = Use_Item()
dict_of_actions = {"Move": move, "Use": use_item}

#    def use_item(character, item_to_add):
#        if item_to_add not in character.items:
#            print("You don't have that on you.")

#    def add_to_active_item(character, item_to_add):
#        pass

#   def use_item(
#       self, item_used
#  ):  ###Used to call battle.update items(), changed it to time sensitive
#     if item_used not in self.items:
#        print("You don't have that on you.")

#           return None
#       if item_used in self.items:
#           self.active_items[item_used] = total_items[item_used]
#           self.items.pop(item_used)
#           if "Soundcloud" in item_used:
#               self.Soundcloud_turn = 2
#           if "G" in item_used:
#               self.G_turn = 1
#######print statements on what item is used

# Move.execute(player, rooms["dance floor"])  # THIS WORKS FINE
# if isinstance(rooms["smoking room"], Room) == True:
#    print("yus")
