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
        debug=False,
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
        self.debug = debug

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
        elif self.high <= 50:
            print("You can feel the high a bit.", end=" ")
        elif self.high <= 70:
            print("This high is feeling goood tho.", end=" ")
        elif self.high <= 90:
            print("You're very fucking high.", end=" ")
        elif self.high >= 100:
            print("You're waay too high right now, like bad high, you feel... ugh.")

        if self.mouth <= 10:  # For mouth
            print("Mouth feels like cardboard, it's really fucking with you.")
        if self.mouth >= 20 and self.mouth <= 40:
            print("Mouth's pretty dry, it's bothering you.")
        if self.mouth >= 50 and self.mouth < 70:
            print("Mouth's feeling a bit dry.")
        if self.mouth >= 70:
            print("")

        if self.lit <= 10:  # For lit
            print("You feel like this party sucks... ", end=" ")
        elif self.lit <= 30:
            print("You're bored. ", end="")
        elif self.lit <= 50:
            print("You're kinda enjoying yourself. ", end=" ")
        elif self.lit <= 70:
            print("You feel like you're having fun. ", end=" ")
        elif self.lit <= 90:
            print("This party's really fucking lit. ", end=" ")
        elif self.lit >= 100:
            print("You're having an amazing time. ", end=" ")

        if self.coolness <= 10:  # For coolness
            print("")
        elif self.coolness <= 40:
            print("Some looks from people.")
        elif self.coolness <= 70:
            print("Getting looks from some cuties around the room.")
        elif self.coolness <= 90:
            print("You're feeling tense. ")
        elif self.coolness >= 100:
            print("You feel very anxious. ")
        print("""			""")

        if self.debug == True:
            print(
                "cool is now",
                self.coolness,
                " , lit is now",
                self.lit,
                ", high is now",
                self.high,
                ", mouth is now",
                self.mouth,
            )

    def update_body(
        self,
    ):  # modifies lit and cool depending on other stats, should be time sensitive.
        if self.debug == True:
            print("running update body in player")
        if self.high >= 30 and self.high < 70:
            self.lit += 10
            self.coolness += 10
        elif self.high >= 70 and self.high < 100:
            self.lit += 20
            self.coolness -= 10
        elif self.high >= 100:
            self.high = 100

        if self.mouth <= 10:  # For mouth
            self.coolness += 10
            self.lit -= 10
            self.mouth = 10
        elif self.mouth >= 20 and self.mouth <= 40:
            self.lit -= 10

        if self.lit > 50:  # For lit
            self.coolness -= 10
        if self.lit > 80:
            self.coolness -= 10

        for attr in ["high", "coolness", "lit", "mouth"]:
            if getattr(self, attr) < 10:
                setattr(self, attr, 10)
                if self.debug == True:
                    print(" fixed now its 10.")
            elif getattr(self, attr) > 100:
                setattr(self, attr, 100)
                if self.debug == True:
                    print("fixed now its 100.")

    def modify_stat(self, attr, ammount, bool):
        """attribute in ""(coolness, high, lit, mouth), ammount in multiples of 10,
        bool True if you want to add, False if you want to substract"""
        assert ammount % 10 == 0
        base_stat = getattr(self, attr)
        if bool == True:
            setattr(self, attr, (base_stat + ammount))
            if self.debug == True:
                print(
                    "Attribute is",
                    attr,
                    "it was",
                    base_stat,
                    "now its",
                    (base_stat + ammount),
                )
        elif bool == False:
            setattr(self, attr, (base_stat - ammount))
            if self.debug == True:
                print(
                    "Attribute is",
                    attr,
                    "it was",
                    base_stat,
                    "now its",
                    (base_stat - ammount),
                )

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
    40,
    0,
    0,
    ["cigarette", "Soundcloud", "blunt"],
    {},
)
