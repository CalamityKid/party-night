from Narration import narrate_items
from Blocks.Player import MainCharacter, player
from Blocks.NPC import NPC, NPCs
from Blocks.Items import items
from Blocks.Time import Time
from Blocks.Room import Room, rooms
from Format import formatting, Bark
import Input
from Actions import dict_of_actions as actions

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


print(formatting.format_objects_string(items))

print(rooms["smoking room"].usable_in_room(items["cigarette"]))
print(rooms["bathroom"].usable_in_room(items["cigarette"]))

print(items["cigarette"].usable_in_room(rooms["smoking room"]))
print(items["cigarette"].usable_in_room(rooms["bathroom"]))

player.location = rooms["smoking room"]
print(player.location)
narrate_items(player)

player.location = rooms["bathroom"]
narrate_items(player)
