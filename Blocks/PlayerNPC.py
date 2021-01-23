class Player:
    def __init__(
        self,
        name,
        lit,
        high,
        coolness,
        items,
        active_items,
        location,
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

    def __repr__(self):
        return "The protagonist, {name}.".format(name=self.name)


class NPC(Player):
    def __init__(
        self, name, items, how_cool, location, times_talked=0, flirt=None
    ):  ###Items are passed in a LIST
        self.name = name
        self.items = items
        self.how_cool = how_cool
        self.location = location
        self.times_talked = times_talked
        self.flirt = flirt

    def __repr__(self):
        return "NPC: " + self.name


###NPCS GO DOWN HERE####       SET UP INPUT KEYS in Battle.identify_user
def setupcharacters(partnerlocation, smilelocation, russianlocation):
    player = Player(
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
        None,
    )
    partner = NPC("your partner", ["cigarette"], 0, partnerlocation)
    smile = NPC("the smile embassador", ["blunt"], 0, smilelocation)
    russian = NPC("your russian friend", ["poppers", "lollipop"], 0, russianlocation)
    tanktop = NPC(
        "the cutie in the tank top",
        ["Soundcloud", "blunt", "cigarette", "lollipop"],
        50,
        None,
    )
    pusher = NPC(
        "someone who seems to be a pusher",
        ["Soundcloud", "blunt", "cigarette", "poppers", "chewing gum"],
        90,
        None,
    )
    hottest = NPC("a breathtaking beauty", ["lollipop", "cigarette"], 90, None)
    couple = NPC(
        "an attractive couple", ["blunt", "cigarette", "chewing gum"], 20, None
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
