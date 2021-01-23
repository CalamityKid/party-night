from Blocks.Room import (
    smoking_room,
    dance_floor,
    bathroom,
    every_room,
)  # import instances of rooms
from Blocks.PlayerNPC import setupcharacters  # imports player and NPC setup method
from Blocks.Scene import Scene, SceneVariables
from Scenes.SmileScenes.Smile0 import smiletimes0content


player, every_character = setupcharacters(None, None, None)
people_in_party = [
    every_character["partner"],
    every_character["smile"],
    every_character["russian"],
]

##############################
# print(smile.times_talked)
# SmileTimes0 = Scene("SmileTimes0", smile, smiletimes0content)
# SmileTimes0.run_scene()
# print(smile.times_talked)
