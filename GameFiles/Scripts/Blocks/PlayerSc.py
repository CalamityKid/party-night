from ..Format.Bark import body_check_bark as body_check_bark


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
        identifiers=["player", "myself", "me"],
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
            ):  # if its a loading item, it ticks the counter and skips its use
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
                ####checks if an item has an exit effect and makes it happen if it does
                if (hasattr(activeitemkey, "exit_effect") == True) and (
                    activeitemkey.exit_effect != None
                ):
                    for (
                        effectkey,
                        effectvalue,
                    ) in (
                        activeitemkey.exit_effect.items()
                    ):  # for each effect in the the exit effects dictionary
                        for attribute in vars(self):  # checks your attributes
                            if (
                                str(attribute) == effectkey
                            ):  # if its the same updates them
                                updated_value = (vars(self)[attribute]) + effectvalue
                                vars(self)[attribute] = updated_value
        self.active_items = updated_list  # returns
        self.update_body()

    def narrate_stats(self, bark=True):  # Informs body stats.
        if bark == True:
            body_check_bark()
        if self.high <= 20:  # For high
            print("Pretty sober rn.", end=" ")
        if self.high >= 30 and self.high <= 50:
            print("You can feel the high a bit.", end=" ")
        if self.high >= 60 and self.high <= 70:
            print("This high is feeling goood tho.", end=" ")
        if self.high >= 80 and self.high <= 90:
            print("Great fucking high, the world is yours.", end=" ")
        if self.high >= 100:
            print("You're waay too high right now, like bad high, you feel... ugh.")

        print("high is now", self.high)

        if self.mouth <= 10:  # For mouth
            print("Mouth feels like cardboard, it's really fucking with you.")
        if self.mouth >= 20 and self.mouth <= 40:
            print("Mouth's pretty dry, it's bothering you.")
        if self.mouth >= 50 and self.mouth < 70:
            print("Mouth's feeling a bit dry.")
        if self.mouth >= 70:
            print("")

        print("mouth is now", self.mouth)

        if self.lit <= 10:  # For lit
            print("You feel like leaving...", end=" ")
        if self.lit >= 20 and self.lit <= 40:
            print("Not really feeling this party.", end=" ")
        if self.lit >= 50 and self.lit <= 70:
            print("You're enjoying yourself.", end=" ")
        if self.lit >= 80 and self.lit <= 90:
            print("This party's really fucking lit.", end=" ")
        if self.lit >= 100:
            print("You're having the best time of your life.", end=" ")

        print("lit is now", self.lit)

        if self.coolness <= 10:  # For coolness
            print("Not getting any attention.")
        if self.coolness >= 20 and self.coolness <= 40:
            print("Not getting much attention.")
        if self.coolness >= 50 and self.coolness <= 70:
            print("Getting looks from cute people.")
        if self.coolness >= 80 and self.coolness <= 90:
            print("Getting the attention of the hottest people.")
        if self.coolness >= 100:
            print("You're the soul of the party.")
        print("""			""")

        print("cool is now", self.coolness)

    def update_body(
        self,
    ):  # modifies lit and cool depending on other stats, should be time sensitive.
        print("running update body in player")
        if self.high >= 30 and self.high <= 50:
            self.lit += 10
        if self.high >= 60 and self.high <= 70:
            self.lit += 20
            self.coolness += 10
        if self.high >= 80 and self.high <= 90:
            self.lit += 30
            self.coolness += 10
        if self.high >= 100:
            self.high = 90
            self.coolness -= 10
            self.lit -= 20

        if self.mouth <= 10:  # For mouth
            self.coolness -= 10
            self.lit -= 10
            self.mouth = 10
        if self.mouth >= 20 and self.mouth <= 40:
            self.lit -= 10

        for attr in ["high", "coolness", "lit", "mouth"]:
            if getattr(self, attr) < 10:
                setattr(self, attr, 10)
                print(" fixed now its 10.")
            elif getattr(self, attr) > 100:
                setattr(self, attr, 100)
                print("fixed now its 100.")

    def narrate(self):
        if self.location == self.rooms["dance floor"]:
            print("You're currently on " + str(self.location) + "... ", end="")
        else:
            print("You're currently in " + str(self.location) + "... ", end="")
        self.narrate_stats(False)


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

player = MainCharacter(
    "main character",
    20,
    0,
    10,
    ["cigarette", "Soundcloud", "blunt"],
    {},
)
