from time import sleep
from .ActionSc import Action
from ..Format.Calculations import (
    calculate_friend_boost,
    calculate_mod_item_effect,
    calculate_bads,
    calculate_goods,
    create_bads_code,
    create_bool_dict,
    create_goods_code,
    calculate_outcome,
    outcome_on_stats,
    create_list_people_in_room,
)
from ..Format.DanceNarration import (
    dance_flourish,
    narrate_bads,
    narrate_goods,
    narrate_opening,
    narrate_outcomes,
)
from ...Scenes.Dance.Compile import dance_scenes


class DanceInstance:
    """holds the modified attributes of each dance instance for calculations, the unmodified are in player
    after the dance action ends the instance isn't used again"""

    pass


class Dance(Action):
    def __init__(
        self,
        name="dance",
        identifiers=["dance", "vogue"],
        rooms_it_cannot_be_done_in=["the smoking room", "the bathroom"],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, player_object, thing_to_be_checked):
        instance = DanceInstance()  # creates instance
        instance.flourish_counter = 1
        dance_flourish(instance)
        people_in_room = create_list_people_in_room(player_object)
        print(narrate_opening(player_object, people_in_room))

        # checks if dance scenes apply
        for person in people_in_room:
            if person.name in dance_scenes:
                dance_scenes[person.name].run_scene(player_object)
                dance_flourish(instance)
                sleep(3)

        # if object_checking.party.music == "" multiplier is 0.8, 1.2 o 1   GET THE MUSIC IN THERE

        # checks item mod effects and assigns them to the instance
        instance.lit = calculate_mod_item_effect(player_object, "lit")
        instance.high = calculate_mod_item_effect(player_object, "high")
        instance.coolness = calculate_mod_item_effect(player_object, "coolness")
        instance.friend_boost = calculate_friend_boost(people_in_room)

        # calculates the goods and bads and the result
        instance.goods = calculate_goods(instance)
        instance.bads = calculate_bads(instance)
        instance.result = int(instance.goods - instance.bads)

        # creates the bool dictionary for narration
        instance.bool_dict = create_bool_dict(instance)
        instance.goods_code = create_goods_code(instance.bool_dict)
        instance.bads_code = create_bads_code(instance)

        """print(
            "dance result is ",
            instance.result,
            "goods:",
            instance.goods,
            "bads:",
            instance.bads,
        )"""

        instance.unmodded_goods = calculate_goods(player_object)
        instance.unmodded_result = int(instance.unmodded_goods - instance.bads)

        """print(
            "unmodded dance result is",
            instance.unmodded_result,
            "unmodded goods:",
            instance.unmodded_goods,
        )

        print(narrate_bads(instance))
        print(narrate_goods(instance))"""
        (num, str) = calculate_outcome(instance.result)
        sleep(3)
        print(narrate_outcomes(num, str))
        outcome_on_stats(
            player_object, num, (num != 1)
        )  # num is the outcome, 1 is bad, so it'll be = to outcome bool

        # instance.good_causes = identify_causes(object_checking, True)
        # instance.good_causes = identify_causes(object_checking, False)
        # instance.good_mod = mod_helped(object_checking, instance, True)
        # instance.bad_mod = mod_helped(object_checking, instance, False)

        dance_flourish(instance)
        return True

    def narrate(self, player_obj):
        if self.doable_in_room(player_obj.location) == True:
            print("You could also [DANCE] here.", end=" ")


dance = Dance()
