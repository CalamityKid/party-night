from GameFiles.Input import player_choose_action
from .Scripts.Format.Narration import (
    narrate_actions,
    narrate_items as narrate_items,
    narrate_people_in_room as narrate_people_in_room,
)

from .Scripts.Blocks import (
    Item as Item,
    items as items,
    MainCharacter as MainCharacter,
    player as player,
    NPC as NPC,
    NPCs as NPCs,
    Room as Room,
    rooms as rooms,
    dict_of_objects as dict_of_objects,
    time as time,
    party as party,
)
from .Scripts.Actions import (
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

########### Gives the player all objects and actions for easier access in functions
player.dict_of_actions = dict_of_actions
player.dict_of_objects = dict_of_objects
player.dict_of_people = NPCs
player.party = party
player.people_in_party = [NPCs["smile"], NPCs["partner"], NPCs["russian"]]

# Gives the player and NPCs a location so shit doesn't crash
player.location = rooms["bathroom"]
NPCs["partner"].location = rooms["bathroom"]
NPCs["smile"].location = rooms["bathroom"]
NPCs["russian"].location = rooms["smoking room"]
NPCs["tanktop"].location = rooms["smoking room"]


# print(formatting.format_objects_string(items))
# print(rooms["smoking room"].usable_in_room(items["cigarette"]))
# print(items["cigarette"].usable_in_room(rooms["bathroom"]))

# narrate_items(player)
# player.narrate_stats()
# player_choose_action()
print("GAME START.")
print("")

while player.gameover == False:
    player_choose_action(player)
    time.ten_minutes()
print("GAME OVER BITCH")
