from .ItemsSc import Item, items
from .PlayerSc import MainCharacter, player
from .NPCSc import NPC, NPCs
from .RoomSc import Room, rooms

__all__ = ["ItemsSc", "PlayerSc", "NPCSc", "RoomSc", "SceneSc", "TimeSc"]


def create_dictionary_of_objects(dict1, dict2, dict3):
    dictionary_of_items = {}
    for key, value in dict1.items():
        dictionary_of_items[key] = value
    for key, value in dict2.items():
        dictionary_of_items[key] = value
    for key, value in dict3.items():
        dictionary_of_items[key] = value
    return dictionary_of_items


dict_of_objects = create_dictionary_of_objects(items, rooms, NPCs)
