from .ActionSc import Action
from ..Format.Bark import flirt_bark_good, flirt_bark_bad


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

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        print(flirt_bark_good(object_performing_the_action))
        print(flirt_bark_bad(object_performing_the_action))
        return None


flirt = Flirt()
