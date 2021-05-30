from Blocks.PlayerNPC import (
    setupcharacters,
    player,
    NPC,
    MainCharacter,
)
from Blocks.Room import rooms, Room
from Blocks.Items import items, Item
import Input

# from Blocks.Scene import Scene, SceneVariables
# from Scenes.SmileScenes.Smile0 import smiletimes0content
NPCs = setupcharacters(None, None, None)

people_in_party = [
    NPCs["partner"],
    NPCs["smile"],
    NPCs["russian"],
]


##############################
# print(smile.times_talked)
# SmileTimes0 = Scene("SmileTimes0", smile, smiletimes0content)
# SmileTimes0.run_scene()
# print(smile.times_talked)
