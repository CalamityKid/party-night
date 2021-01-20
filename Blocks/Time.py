class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        if self.minute == 0:
            return "0{hour}:0{minute}".format(hour=self.hour, minute=self.minute)
        else:
            return "0{hour}:{minute}".format(hour=self.hour, minute=self.minute)

    #    def thirty_minute_update(self):
    #       Battle.body_check()

    def fast_acting(self):  # for item effects that are immediate
        return None  # should find a way around this

    def ten_minutes(self):
        time.minute += 10
        Battle.update_items()

        #        if time.minute % 30 == 0:
        #            time.thirty_minute_update()

        if time.minute == 60:
            time.hour += 1
            time.minute = 0

        if time.hour == 6:
            player.gameover = True
            print("GAME OVER")