from .ActionSc import Action
from ..Blocks.PlayerSc import MainCharacter
from ...Scenes.SceneSelectSc import scene_select
from ..Format.formatting import format_objects_string
from ..Format.Calculations import create_list_people_in_room


class Talk(Action):
    def __init__(
        self,
        name="talk to someone",
        identifiers=["talk", "tal"],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, person_talking, thing_to_talk_to):
        if isinstance(thing_to_talk_to, MainCharacter) == True:
            if thing_to_talk_to == person_talking:
                print("You can't talk to yourself")
                return None
            if thing_to_talk_to.location != person_talking.location:
                print("They're not here right now.")
                return None
            elif thing_to_talk_to.location == person_talking.location:
                return scene_select(person_talking, thing_to_talk_to)
        elif isinstance(thing_to_talk_to, MainCharacter) != True:
            print("You can't talk to " + str(thing_to_talk_to.name) + ".")
            return None

    def narrate(self, player_obj):
        people_in_room_string = ""
        people_in_room_list = create_list_people_in_room(player_obj)
        if player_obj.NPCs["partner"] in people_in_room_list:
            people_in_room_list.remove(player_obj.NPCs["partner"])
            people_in_room_string = format_objects_string(people_in_room_list)
        if people_in_room_string == "nothing":
            people_in_room_string = "no familiar faces."
        else:
            print("")
        print("You see " + people_in_room_string, end=" ")
        if people_in_room_string != "no familiar faces.":
            print("You could [FLIRT] or [TALK] to them.")
        else:  # to keep the spacing equal cause of the end
            print("")


talk = Talk()
