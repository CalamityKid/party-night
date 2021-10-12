str1 = "this is a string"
dict1 = {"a": 1, "b": 2, "c": 3}
lst = ["a", "b", "c", "d", "e"]


class wv(object):
    def __init__(self, hand):
        self.hand = hand

    def yield_hand(self):
        for y in self.hand:
            yield y

    def print(self):
        for i in self.yield_hand():
            if i != None:
                print(i)


hand1 = wv(dict1)

hand1.print()
