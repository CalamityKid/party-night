class Item:
    def __init__(
        self,
        name,
        identifiers,
        duration,
        use_text,
        active_item_text,
        effects_while_active,
        exit_text,
        narrate_text,
        rooms_it_cannot_be_done_in=None,
        loading_item=False,
        loading_counter=None,
        loading_text=None,
    ):
        self.name = name
        self.identifiers = identifiers
        self.duration = duration
        self.use_text = use_text
        self.active_item_text = active_item_text
        self.loading_item = loading_item
        self.loading_text = loading_text
        self.effects_while_active = effects_while_active
        self.exit_text = exit_text
        self.narrate_text = narrate_text
        self.loading_counter = loading_counter
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def __repr__(self):
        return self.name

    def usable_in_room(self, room_youre_in):
        try:
            if room_youre_in.name in self.rooms_it_cannot_be_done_in:
                return False
            elif room_youre_in.name not in self.rooms_it_cannot_be_done_in:
                return True
        except TypeError:
            return True

    def narrate(self):
        print(self.narrate_text)


#########################################################################
#############################   INSTANCES   #############################
#########################################################################


def setupitems():
    lollipop = Item(
        "a lollipop",
        ["lol"],
        50,
        "You put the lollipop in your mouth.",
        "You're sucking on the lollipop.",
        {"mouth": 30, "coolness": 10},
        "You chew on the lollipop and gulp it down.",
        "Sucking on a lollipop makes look AND taste sexy.",
    )
    soundcloud = Item(
        "a Soundcloud pill",
        ["sound", "pill", "mdma"],
        70,
        "You pop the pill.",
        "You can't help your body moving to the music. Soundcloud's coming up.",
        {"high": 20, "lit": 20, "mouth": -20},
        "You don't feel the pill high anymore.",
        "Soundcloud makes you fly, watch the cotton mouth though.",
        None,
        True,
        20,
        "Soundcloud's still loading it seems.",
    )
    ghb = Item(
        "G",
        ["ghb", "chorr"],
        40,
        "You mix the G with some water and wash it down in a big gulp.",
        "G's making you horny af.",
        {"high": 10, "lit": 20},
        "You don't feel the G anymore.",
        "G's like alcohol but better, unless you mix it with alcohol. Then it's like poison.",
        ["the dance floor", "the smoking room"],
        True,
        20,
        "G still hasn't kicked in...",
    )
    blunt = Item(
        "a blunt",
        ["blunt", "weed", "hash", "maria", "green"],
        50,
        "Puff, puff, pass.",
        "The blunt's buzzing in the background",
        {"coolness": 10, "high": 10, "lit": 10, "mouth": -20},
        "The green high fades away.",
        "Marijuana. Not even once. Well, maybe a few times.",
        ["the dance floor", "the bathroom"],
    )
    cigarette = Item(
        "a cigarette",
        ["cig", "gare"],
        20,
        "You smoke the cigarette.",
        "You feel the nicotine.",
        {"coolness": 20, "lit": 10, "high": 10, "mouth": -10},
        "You don't feel the nicotine anymore.",
        "Cancer sticks. Look cool, die faster.",
        ["the dance floor", "the bathroom"],
    )
    poppers = Item(
        "a bottle of poppers",
        ["popp", "rush"],
        20,
        "You huff in the vapors.",
        "Oof, the poppers.",
        {"high": 10, "lit": 30},
        "Popper comedown. Alright.",
        "Poppers. To the moon and back in 30 seconds.",
        ["the smoking room"],
    )
    chewing_gum = Item(
        "some chewing gum",
        ["chew", "gum", "mint"],
        40,
        "You put the chewing gum in your mouth.",
        "Gum's still minty fresh",
        {"mouth": 30},
        "Chewing gum's tasteless, you get rid of it.",
        "Chewing gum, an oasis in your mouth.",
    )
    return {
        "lollipop": lollipop,
        "Soundcloud": soundcloud,
        "G": ghb,
        "blunt": blunt,
        "cigarette": cigarette,
        "poppers": poppers,
        "chewing gum": chewing_gum,
    }


items = setupitems()
