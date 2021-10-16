from .ActionSc import Action
from ..Format.Calculations import (
    calculate_friend_boost,
    calculate_mod_item_effect,
    outcome,
    calculate_bads,
    calculate_goods,
)
from ..Format.DanceNarration import identify_causes, mod_helped, narrate_goods


class DanceInstance:
    """holds the modified attributes of each dance instance for calculations, the unmodified are in player
    after the dance action ends the instance isn't used again"""

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
        instance = DanceInstance()  # creates instance
        # if object_checking.party.music == "" multiplier is 0.8, 1.2 o 1   GET THE MUSIC IN THERE

        # checks item mod effects and assigns them to the instance
        instance.lit = calculate_mod_item_effect(player_object, "lit")
        instance.high = calculate_mod_item_effect(player_object, "high")
        instance.coolness = calculate_mod_item_effect(player_object, "coolness")
        instance.friend_boost = calculate_friend_boost(player_object)

        # calculates the goods and bads and the result
        instance.goods = calculate_goods(instance)
        instance.bads = calculate_bads(instance)
        instance.result = int(instance.goods - instance.bads)

        #

        print(
            "dance result is ",
            instance.result,
            outcome(instance.result),
            "goods:",
            instance.goods,
            "bads:",
            instance.bads,
        )

        instance.unmodded_goods = calculate_goods(player_object)
        instance.unmodded_result = int(instance.unmodded_goods - instance.bads)

        print(
            "unmodded dance result is",
            instance.unmodded_result,
            outcome(instance.unmodded_result),
            "unmodded goods:",
            instance.unmodded_goods,
        )
        narrate_goods(instance)

        # instance.good_causes = identify_causes(object_checking, True)
        # instance.good_causes = identify_causes(object_checking, False)
        # instance.good_mod = mod_helped(object_checking, instance, True)
        # instance.bad_mod = mod_helped(object_checking, instance, False)

        return None


dance = Dance()
