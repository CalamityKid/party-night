from .ActionSc import Action
from ..Blocks.PlayerSc import MainCharacter
from ...Scenes.SceneSelectSc import scene_select


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


talk = Talk()
