class Room:
    def __init__(self, name, available_actions, usable_items):
        self.name = name
        self.available_actions = available_actions
        self.usable_items = usable_items

    def __repr__(self):
        return self.name
