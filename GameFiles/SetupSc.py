from time import sleep
from GameFiles.ScheduleSc import update_schedule
from GameFiles.Input import player_choose_action, yesorno
from GameFiles.Scripts.Format.Narration import (
    narrate_actions,
)
from GameFiles.Scenes.PartnerScenes.Compile import partnerscenes
from GameFiles.Scenes.TutorialContent import tutorialscene

# from GameFiles.Scenes.SceneSelectSc import scene_select
from .Scripts.Blocks.SceneSc import scenevariables

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

from .Scenes.Gameover.Compile import assemble_and_run_gameover_scenes

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
player.time = time
player.rooms = rooms
player.NPCs = NPCs
player.people_in_party = [NPCs["smile"], NPCs["partner"], NPCs["russian"]]
player.scenevariables = scenevariables
player.partnerscenes = partnerscenes

# Gives the player and NPCs a location so shit doesn't crash
player.location = rooms["smoking room"]
NPCs["partner"].location = rooms["dance floor"]
NPCs["smile"].location = rooms["dance floor"]
NPCs["russian"].location = rooms["dance floor"]

print("GAME START.")
print("")


time.hour = 00
time.minute = 00

print("Tutorial? (y/n) ", end="")
op = yesorno()
if op == True:
    tutorialscene.run_scene(player)

non_counter = 0
update_schedule()

while player.gameover == False:
    action_met = None
    narrate_actions(player)
    sleep(1)
    player.narrate_stats(True)
    action_met = player_choose_action(player)
    sleep(2)
    if action_met == True or non_counter == 3:
        time.ten_minutes()
        non_counter = 0
    elif action_met != True:
        non_counter += 1

    if player.gameover == False:
        update_schedule()
        sleep(3)

assemble_and_run_gameover_scenes(player)
