class Action:
    def __init__(
        self,
        name,
        identifiers,
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def __repr__(self):
        return str(self.name)

    def doable_in_room(self, action):
        try:
            if action.name in self.rooms_it_cannot_be_done_in:
                return False
            elif action.name not in self.rooms_it_cannot_be_done_in:
                return True
        except TypeError:
            return True
