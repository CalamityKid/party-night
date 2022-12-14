from .ActionSc import Action
from ..Blocks.SceneSc import Scene
from ...Scenes.Gameover.Leave import leavepartycontent

leavescene = Scene("Leave Party Scene", leavepartycontent)


class Leave(Action):
    def __init__(
        self,
        name="leave the party",
        identifiers=[
            "leave",
        ],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, player_object, notused):
        return leavescene.run_scene(player_object)

    def narrate(self, player):
        print("You can [LEAVE] the party at any time.")


leave = Leave()
