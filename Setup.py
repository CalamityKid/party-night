from Narration import narrate_items, narrate_people_in_room
from Scripts.Blocks import (
    Item as Item,
    items as items,
    MainCharacter as MainCharacter,
    player as player,
    NPC as NPC,
    NPCs as NPCs,
    Room as Room,
    rooms as rooms,
)
from Scripts.Actions import (
    Move as Move,
    move as move,
    Use_Item as Use_Item,
    use_item as use_item,
    dict_of_actions as dict_of_actions,
)

# function to give the players item objects
def string_item_to_item_object(character, item_dictionary):
    for stringitem in character.stringitems:
        for key, value in item_dictionary.items():
            if stringitem == key:
                character.items.append(value)


# giving them all giving them all item objects
for key, value in NPCs.items():
    string_item_to_item_object(value, items)
string_item_to_item_object(player, items)


# print(formatting.format_objects_string(items))
# print(rooms["smoking room"].usable_in_room(items["cigarette"]))
# print(items["cigarette"].usable_in_room(rooms["bathroom"]))
# narrate_items(player)

player.location = rooms["smoking room"]
NPCs["partner"].location = rooms["smoking room"]
NPCs["smile"].location = rooms["smoking room"]
NPCs["russian"].location = rooms["bathroom"]
NPCs["tanktop"].location = rooms["bathroom"]
# NPCs["pusher"] = rooms["smoking room"]
NPCs["hottest"].location = rooms["dance floor"]
NPCs["couple"].location = rooms["bathroom"]

player.location = rooms["bathroom"]
narrate_people_in_room(player, NPCs)

player.location = rooms["smoking room"]
narrate_people_in_room(player, NPCs)

player.location = rooms["dance floor"]
narrate_people_in_room(player, NPCs)

NPCs["hottest"].location = rooms["bathroom"]
narrate_people_in_room(player, NPCs)
