class Time:
    def __init__(self, hour, minute, identifiers="time"):
        self.hour = hour
        self.minute = minute
        self.identifiers = identifiers

    def __repr__(self):
        if self.minute == 0:
            return "0{hour} o' clock.".format(hour=self.hour)
        else:
            return "0{hour}:{minute}".format(hour=self.hour, minute=self.minute)

    def thirty_minute_update(self, whereverthebodycheckis):
        whereverthebodycheckis.body_check()

    def ten_minutes(self, whateversystemmanagesitemstoupdate):
        self.minute += 10

        whateversystemmanagesitemstoupdate.update_items()

        if self.minute % 30 == 0:
            self.thirty_minute_update()

        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        if self.hour == 6:
            # player.gameover = True
            print("GAME OVER")

    def narrate(self):
        print("It is now", self)


time = Time(1, 30)
