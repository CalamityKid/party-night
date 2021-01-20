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