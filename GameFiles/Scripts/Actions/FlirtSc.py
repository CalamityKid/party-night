from .ActionSc import Action
from ..Blocks.PlayerSc import MainCharacter
from ...Scenes.Flirt.Compile import flirtscenes


class Flirt(Action):
    def __init__(
        self,
        name="flirt with someone",
        identifiers=[
            "flirt",
        ],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, flirter, flirtee):
        if isinstance(flirtee, MainCharacter) != True:
            print("You can't flirt with ", flirtee.name)
            return True
        if flirtee.location != flirter.location:
            print("They're not here right now.")
            return None
        elif flirtee.location == flirter.location:
            if flirter.debug == True:
                print(
                    "before scene, flirt is {flirtnumber}".format(
                        flirtnumber=flirtee.flirt
                    )
                )
            return flirtscenes[flirtee.name].run_scene(flirter)

    def narrate(self, player):
        return None


flirt = Flirt()
