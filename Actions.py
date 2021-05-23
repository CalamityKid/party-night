from Blocks.Room import Room, rooms

from Blocks.PlayerNPC import MainCharacter, NPC, player, NPCs
from Blocks.Items import Item, items


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
        return ("the action ", self.name)


class Move(Action):
    def __init__(self, name, identifiers, rooms_it_cannot_be_done_in=None):
        self.name = "Move"
        self.identifiers = ["move", "go"]

    def execute(object_performing_the_action, object_to_be_interacted_with):

        if object_performing_the_action.location == object_to_be_interacted_with:
            print("You're already in this room.")
            return None
        elif object_performing_the_action.location != object_to_be_interacted_with:
            if isinstance(object_to_be_interacted_with, Room) == True:
                object_performing_the_action.location = object_to_be_interacted_with
                print(
                    object_performing_the_action.name,
                    "moves to ",
                    object_to_be_interacted_with.name + ".",
                )
            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("DEBUGGING the object you passed is NOT a room.")
                return None


class Use_Item(Action):
    def __init__(self, name, identifiers, rooms_it_cannot_be_done_in=None):
        self.name = "Use"
        self.identifiers = ["use", "item", "smoke", "take"]

    def execute(object_performing_the_action, object_to_be_interacted_with):
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


dict_of_actions = {"Move": Move, "Use": Use_Item}
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
