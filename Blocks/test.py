    def body_check(self): # should be called AFTER update items.
        #CALL a bark function. body_check_opener()
        if self.high <= 20:  # For high
            print("Pretty sober rn.", end=" ")
        if self.high >= 30 and self.high <= 50:
            print("You can feel the high a bit.", end=" ")
            self.lit += 10
        if self.high >= 60 and self.high <= 70:
            print("This high is feeling goood tho.", end=" ")
            self.lit += 20
            self.coolness += 10
        if self.high >= 80 and self.high <= 90:
            print("Great fucking high, the world is yours.", end=" ")
            self.lit += 30
            self.coolness += 10
        if self.high >= 100:
            print("You're waay too high right now, like bad high, you feel... ugh.")
            self.high = 90
            self.coolness -= 10
            self.lit -= 20

        if self.mouth <= 10:  # For mouth
            print("Mouth feels like cardboard, it's really fucking with you.")
            self.coolness -= 10
            self.lit -= 20
            self.mouth = 10
        if self.mouth >= 20 and self.mouth <= 40:
            print("Mouth's getting pretty dry, it's bothering you.")
            self.lit -= 10
        if self.mouth >= 50 and self.mouth < 70:
            print("Mouth's starting to feel a bit dry.")

        if self.lit <= 10:  # For lit
            print("You feel like leaving...", end=" ")
            self.lit = 10
        if self.lit >= 20 and self.lit <= 40:
            print("Not really feeling this party.", end=" ")
        if self.lit >= 50 and self.lit <= 70:
            print("You're enjoying yourself.", end=" ")
        if self.lit >= 80 and self.lit <= 90:
            print("This party's really fucking lit.", end=" ")
        if self.lit >= 100:
            print("You're having the best time of your life.")

        if self.coolness <= 10:  # For coolness
            print("Not getting any attention.")
            self.coolness = 10
        if self.coolness >= 20 and self.coolness <= 40:
            print("Not getting much attention.")
        if self.coolness >= 50 and self.coolness <= 70:
            print("Getting looks from cute people.")
        if self.coolness >= 80 and self.coolness <= 90:
            print("Getting the attention of the hottest people.")
        if self.coolness >= 100:
            print("You're the soul of the party.")
        print("""			""")