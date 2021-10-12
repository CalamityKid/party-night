class Party:
    def __init__(
        self, name="Party", identifiers=["party", "music"], music="great", crowd="empty"
    ):
        self.name = name
        self.music = music
        self.crowd = crowd
        self.identifiers = identifiers

    def __repr__(self):
        return self.name

    def narrate_music(self):
        print("The music is pretty " + self.music + " rn. ", end="")

    def narrate_crowd(self):
        final_string = ""
        if self.crowd == "half":
            final_string += "Party's sorta crowded but you can still move around."
        elif self.crowd == "empty":
            final_string += "Just a few people in the room, party's kinda empty."
        elif self.crowd == "full":
            final_string += "Party's packed full of people."
        print(final_string)

    def narrate(self):
        self.narrate_music()
        self.narrate_crowd()

    def change_music_great(self):
        self.music = "great"

    def change_music_ok(self):
        self.music = "ok"

    def change_music_terrible(self):
        self.music = "terrible"

    def change_crowd_empty(self):
        self.crowd = "empty"

    def change_crowd_full(self):
        self.crowd = "full"

    def change_crowd_half(self):
        self.crowd = "half"


party = Party()
