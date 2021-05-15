class MainCharacter:
    def __init__(
        self,
        name,
        lit,
        high,
        coolness,
        items,
        active_items,
        location=None,
        identifiers=[["player", "myself", "me"]],
        memories=[],
        gameover=False,
    ):
        self.name = name
        self.lit = lit
        self.high = high
        self.coolness = coolness
        self.items = items
        self.active_items = active_items
        self.mouth = 100
        self.Soundcloud_turn = None
        self.G_turn = None
        self.location = location
        self.memories = memories
        self.gameover = gameover
        self.identifiers = identifiers

    def __repr__(self):
        return "The protagonist, {name}.".format(name=self.name)


class NPC(MainCharacter):
    def __init__(
        self, name, items, identifiers, location=None, times_talked=0, flirt=None
    ):  ###Items are passed in a LIST
        self.name = name
        self.items = items
        self.location = location
        self.times_talked = times_talked
        self.flirt = flirt
        self.identifiers = identifiers

    def __repr__(self):
        return "NPC: " + self.name


###NPCS GO DOWN HERE####       SET UP INPUT KEYS in Battle.identify_user
def setupcharacters(partnerlocation=None, smilelocation=None, russianlocation=None):
    player = MainCharacter(
        "Joel",
        20,
        0,
        10,
        {
            "lollipop": 50,
            "Soundcloud": 70,
            "blunt": 40,
            "poppers": 20,
            "chewing gum": 40,
        },
        {},
    )
    partner = NPC("your partner", ["cigarette"], ["part"], partnerlocation)
    smile = NPC(
        "the smile embassador", ["blunt"], ["smil", "embass", "ruben"], smilelocation
    )
    russian = NPC(
        "your russian friend",
        ["poppers", "lollipop"],
        ["russ", "friend", "misha"],
        russianlocation,
    )
    tanktop = NPC(
        "the cutie in the tank top",
        ["Soundcloud", "blunt", "cigarette", "lollipop"],
        ["cut", "tank", "top"],
    )
    pusher = NPC(
        "someone who seems to be a pusher",
        ["Soundcloud", "blunt", "cigarette", "poppers", "chewing gum"],
        ["push"],
    )
    hottest = NPC("a breathtaking beauty", ["lollipop", "cigarette"], ["beau", "breat"])
    couple = NPC(
        "an attractive couple",
        ["blunt", "cigarette", "chewing gum"],
        ["attrac", "coupl"],
    )

    return player, {
        "partner": partner,
        "smile": smile,
        "russian": russian,
        "tanktop": tanktop,
        "pusher": pusher,
        "hottest": hottest,
        "couple": couple,
    }
