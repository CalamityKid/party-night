from .PlayerSc import player


class Time:
    def __init__(self, hour, minute, identifiers="time"):
        self.hour = hour
        self.minute = minute
        self.identifiers = identifiers

    def __repr__(self):
        if self.minute == 0:
            return "0{hour} o' clock.".format(hour=self.hour)
        else:
            return "0{hour}:{minute}.".format(hour=self.hour, minute=self.minute)

    def narrate(self):
        print("It is now " + str(self))

    def thirty_minute_update(self):
        self.narrate()
        player.party.narrate()
        player.narrate()

    def ten_minutes(self):
        self.minute += 10

        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        if self.hour == 6:
            player.gameover = True
            print("GAME OVER")
            ##############RUN GAMEOVER SCRIPT##############

        if player.gameover == True:
            return None

        elif player.gameover == False:
            if self.minute == 00 or self.minute == 30:
                player.high -= 10
                if player.party.music == "great":
                    player.lit += 10
                    print("The music's fire rn, it's cheering you up.")
                elif player.party.music == "terrible":
                    player.lit -= 10
                    print("You really hate this music.")
                self.thirty_minute_update()
            player.update_active_items()
            print("")


time = Time(00, 00)
