from .PlayerSc import player


class Time:
    def __init__(self, hour, minute, identifiers="time"):
        self.hour = hour
        self.minute = minute
        self.identifiers = identifiers

    def __repr__(self):
        if self.hour == 0 and self.minute == 0:
            return "Midnight."
        if self.minute == 0:
            return "0{hour} o' clock.".format(hour=self.hour)
        else:
            return "0{hour}:{minute}.".format(hour=self.hour, minute=self.minute)

    def narrate(self):
        print("It is now " + str(self))

    def ten_minutes(self):
        self.minute += 10

        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        if self.hour == 6:
            player.gameover = True
            print("")
            print("The lights turn on!")
            print("It's 6 am!")
            print("")
            ##############RUN GAMEOVER SCRIPT##############

        if player.gameover == True:
            return None

        elif player.gameover == False:
            if self.minute == 00 or self.minute == 30:
                player.high -= 10
                if player.location.name == "the dance floor":
                    if player.party.music == "great":
                        player.lit += 10
                        print("The music's fire rn. You're really feeling it.")
                    elif player.party.music == "terrible":
                        player.lit -= 10
                        player.coolness += 10
                        print("You really hate this music.")
            player.update_active_items()
            print("")


time = Time(00, 00)
