class MainCharacter:
    def __init__(
        self,
        name,
        lit,
        high,
        coolness,
        stringitems,
        active_items,
        items=[],
        location=None,
        identifiers=[["player", "myself", "me"]],
        memories=[],
        gameover=False,
    ):
        self.name = name
        self.lit = lit
        self.high = high
        self.coolness = coolness
        self.stringitems = stringitems
        self.active_items = active_items
        self.mouth = 100
        self.Soundcloud_turn = None
        self.G_turn = None
        self.location = location
        self.memories = memories
        self.gameover = gameover
        self.identifiers = identifiers
        self.items = items

    def __repr__(self):
        return "The protagonist, {name}.".format(name=self.name)

    def update_active_items(
        self,
    ):  # Item effects happen and list is updated, should happen every 10 minutes
        updated_list = {}
        for activeitemkey, activeitemvalue in self.active_items.items():
            updated_value = 0
            if (
                activeitemkey.loading_item == True
            ):  # if its a loading item, it ticks the clock and skips its use
                if activeitemkey.loading_counter > 0:  # that isnt done loading
                    activeitemkey.loading_counter -= 10  # it ticks the counter
                    print(activeitemkey.loading_text)  # prints the text
                    updated_list[
                        activeitemkey
                    ] = activeitemvalue  # keeps it in active items
                    continue  # and passes
            activeitemvalue = activeitemvalue - 10  # wanes the effect
            if activeitemvalue > 0:
                print(
                    activeitemkey.active_item_text
                )  # prints the use text # Then comes the effects
                for (
                    effectkey,
                    effectvalue,
                ) in (
                    activeitemkey.effects_while_active.items()
                ):  # for each effect in the item dictionary
                    for attribute in vars(self):  # checks your attributes
                        if str(attribute) == effectkey:  # if its the same
                            updated_value = (vars(self)[attribute]) + effectvalue
                            vars(self)[attribute] = updated_value  # changes that value
                            # print("Now ", attribute, "is ", vars(self)[attribute])
            if activeitemvalue > 0:  # adds it back if it hasn't waned off
                updated_list[activeitemkey] = activeitemvalue
            elif activeitemvalue <= 0:
                print(activeitemkey.exit_text)
        self.active_items = updated_list


class NPC(MainCharacter):
    def __init__(
        self,
        name,
        stringitems,
        identifiers,
        location=None,
        times_talked=0,
        flirt=None,
        items=[],
    ):
        self.name = name
        self.stringitems = stringitems
        self.location = location
        self.times_talked = times_talked
        self.flirt = flirt
        self.identifiers = identifiers
        self.stringitems = stringitems
        self.items = []

    def __repr__(self):
        return "NPC: " + self.name


###################################### player + character instances
player = MainCharacter(
    "main character",
    20,
    0,
    10,
    ["lollipop", "Soundcloud", "blunt", "poppers", "chewing gum"],
    {},
)


def setupcharacters(partnerlocation=None, smilelocation=None, russianlocation=None):
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

    return {
        "partner": partner,
        "smile": smile,
        "russian": russian,
        "tanktop": tanktop,
        "pusher": pusher,
        "hottest": hottest,
        "couple": couple,
    }


NPCs = setupcharacters()
