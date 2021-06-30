from .ActionSc import Action
from ..Format.Calculations import calculate_friend_boost, calculate_mod_item_effect


class DanceInstance:
    pass

class Dance(Action):
    def __init__(
        self,
        name="dance",
        identifiers=["dance", "vogue"],
        rooms_it_cannot_be_done_in=[],  # "the smoking room", "the bathroom"
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_checking, thing_to_be_checked):
        instance = DanceInstance()
        if object_checking.party.music == "" multiplier is 0.8, 1.2 o 1

        instance.mod_lit = calculate_mod_item_effect(object_checking, "lit")
        instance.mod_high = calculate_mod_item_effect(object_checking, "high")
        instance.mod_cool = calculate_mod_item_effect(object_checking, "coolness")
        instance.friend_boost = calculate_friend_boost(object_checking)

        instance.result = ((instance.mod_lit + instance.mod_high) / 2) - (instance.mod_cool - instance.friend_boost)
        print("dance result is ", instance.result)
        GET THE MUSIC IN THERE

        return None


dance = Dance()
