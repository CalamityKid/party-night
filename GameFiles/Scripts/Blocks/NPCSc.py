from .PlayerSc import MainCharacter, player


class NPC(MainCharacter):
    def __init__(
        self,
        name,
        stringitems,
        identifiers,
        location=None,
        times_talked=0,
        flirt=0,
        items=[],
        boost=1.1,
    ):
        self.name = name
        self.stringitems = stringitems
        self.location = location
        self.times_talked = times_talked
        self.flirt = flirt
        self.identifiers = identifiers
        self.stringitems = stringitems
        self.items = items
        self.boost = boost

    def __repr__(self):
        return "NPC: " + self.name

    def narrate(self):
        if player.location == self.location:
            print("You see " + self.name + " nearby.")
        elif player.location != self.location:
            print("You can't see " + self.name + " around.")


#########################################################################
#############################   INSTANCES   #############################
#########################################################################


def setupcharacters(partnerlocation=None, smilelocation=None, russianlocation=None):
    partner = NPC("your partner", ["cigarette"], ["part"], partnerlocation)
    smile = NPC(
        "the smile ambassador", ["blunt"], ["smil", "ambass", "ruben"], smilelocation
    )
    russian = NPC(
        "your russian friend",
        ["poppers", "lollipop"],
        ["russ"],
        russianlocation,
    )
    tanktop = NPC(
        "the cutie in the tank top",
        ["Soundcloud", "blunt", "cigarette", "lollipop"],
        ["cutie", "tank", "tanktop"],
    )
    pusher = NPC(
        "someone who seems to be a pusher",
        ["Soundcloud", "blunt", "cigarette", "poppers", "chewing gum"],
        ["pusher"],
    )
    couple = NPC(
        "the attractive couple",
        ["blunt", "cigarette", "chewing gum"],
        ["attrac", "coupl"],
    )

    return {
        "partner": partner,
        "smile": smile,
        "russian": russian,
        "tanktop": tanktop,
        "pusher": pusher,
        "couple": couple,
    }


NPCs = setupcharacters()
