from .ActionSc import Action
from GameFiles.Input import yesorno
from GameFiles.Scenes.TutorialContent import tutorialscene


class Tutorial(Action):
    def __init__(
        self,
        name="play tutorial",
        identifiers=["tutorial"],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        print("Do yo want to run the tutorial? (y/n) ", end="")
        op = yesorno()
        if op == True:
            tutorialscene.run_scene(object_performing_the_action)
        elif op == False:
            print("You can do the tutorial at any time by writing [TUTORIAL]")
        return None

    def narrate(self, player_obj):
        return None


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

tutorial = Tutorial()
