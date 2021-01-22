class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        if self.minute == 0:
            return "0{hour}:0{minute}".format(hour=self.hour, minute=self.minute)
        else:
            return "0{hour}:{minute}".format(hour=self.hour, minute=self.minute)

    def thirty_minute_update(self, whereverthebodycheckis):
        whereverthebodycheckis.body_check()

    def fast_acting(self):  # for item effects that are immediate
        return None  # should find a way around this

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


time = Time(1, 30)