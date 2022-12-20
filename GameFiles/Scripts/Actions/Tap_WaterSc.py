from .ActionSc import Action
from time import sleep


class Tap_Water(Action):
    def __init__(
        self,
        name="drink tap water",
        identifiers=["drink", "tap"],
        rooms_it_cannot_be_done_in=["the dance floor", "the smoking room"],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        if (
            object_performing_the_action.location.name
            in self.rooms_it_cannot_be_done_in
        ):
            print("You can only drink tap water in the bathroom.")
            return None
        print("It's definitely not your best look, but free water is free water.")
        sleep(2)
        print("You get your head in the sink and take a few gulps. ", end="")
        sleep(2)
        print("It's refreshing.")
        object_performing_the_action.coolness -= 10
        object_performing_the_action.mouth += 30
        return True

    def narrate(self, player_obj):
        if self.doable_in_room(player_obj.location) == True:
            print("You could [DRINK TAP] water too.", end=" ")


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

tap_water = Tap_Water()
