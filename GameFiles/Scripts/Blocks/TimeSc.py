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
        # update schedule
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
            if self.minute % 30 == 0:
                player.high -= 10
                self.thirty_minute_update()
            player.update_active_items()
            print("")


time = Time(1, 00)