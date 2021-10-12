from .ActionSc import Action
from ..Format.Calculations import (
    calculate_friend_boost,
    calculate_mod_item_effect,
)
from ..Format.DanceNarration import identify_causes, mod_helped


class DanceInstance:
    pass


class Dance(Action):
    def __init__(
        self,
        name="dance",
        identifiers=["dance", "vogue"],
        rooms_it_cannot_be_done_in=[],
        # "the smoking room", "the bathroom"
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, player_object, thing_to_be_checked):
        instance = DanceInstance()
        # if object_checking.party.music == "" multiplier is 0.8, 1.2 o 1   GET THE MUSIC IN THERE

        instance.mod_lit = calculate_mod_item_effect(player_object, "lit")
        instance.mod_high = calculate_mod_item_effect(player_object, "high")
        instance.mod_coolness = calculate_mod_item_effect(player_object, "coolness")
        instance.friend_boost = calculate_friend_boost(player_object)

        instance.result = ((instance.mod_lit + instance.mod_high) / 2) - (
            instance.mod_coolness - instance.friend_boost
        )
        print("dance result is ", instance.result)

        instance.unmodded_result = ((player_object.lit + player_object.high) / 2) - (
            player_object.coolness - instance.friend_boost
        )
        print("unmodded dance result is", instance.unmodded_result)
        # instance.good_causes = identify_causes(object_checking, True)
        # instance.good_causes = identify_causes(object_checking, False)
        # instance.good_mod = mod_helped(object_checking, instance, True)
        # instance.bad_mod = mod_helped(object_checking, instance, False)

        return None


dance = Dance()
