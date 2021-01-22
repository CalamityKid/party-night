from Blocks.Room import *  # import Room class and also instances
from Blocks.PlayerNPC import Player, NPC
from Blocks.Scene import Scene, SceneVariables
from Scenes.SmileScenes.Smile0 import smiletimes0content
from Blocks.Room import *

###ROOM SETUP GOES BELOW###
# ("name" must be compatible with "the name" formula, [available actions], [usable items])
# Moods are "okay", "great music", "terrible music"###
smoking_room = Room(
    "the smoking room",
    ["[FLIRT]", "[BORROW] something", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "blunt", "cigarette", "chewing gum"],
)
bathroom = Room(
    "the bathroom",
    ["[FLIRT]", "drink [TAP] water", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "G", "poppers", "chewing gum"],
)
dance_floor = Room(
    "the dance floor",
    [
        "[FLIRT]",
        "[DANCE]",
        "[BORROW] something",
        "[MOVE] to another room",
        "[LEAVE] the party",
    ],
    ["lollipop", "Soundcloud", "poppers", "chewing gum"],
)

every_room = [smoking_room, bathroom, dance_floor]

# remember to add borrow to the actions available in rooms in the tutorial
###ROOM SETUP ABOVE, Every new room must also be set up in Battle.move()###


player = Player(
    "Joel",
    20,
    0,
    10,
    {"lollipop": 50, "Soundcloud": 70, "blunt": 40, "poppers": 20, "chewing gum": 40},
    {},
    smoking_room,
)

###NPCS GO DOWN HERE####       SET UP INPUT KEYS in Battle.identify_user
partner = NPC("your partner", ["cigarette"], 0, smoking_room)
smile = NPC("the smile embassador", ["blunt"], 0, bathroom)
misha = NPC("your russian friend", ["poppers", "lollipop"], 0, dance_floor)
tanktop = NPC(
    "the cutie in the tank top",
    ["Soundcloud", "blunt", "cigarette", "lollipop"],
    50,
    dance_floor,
)
pusher = NPC(
    "someone who seems to be a pusher",
    ["Soundcloud", "blunt", "cigarette", "poppers", "chewing gum"],
    90,
    bathroom,
)
hottest = NPC("a breathtaking beauty", ["lollipop", "cigarette"], 90, smoking_room)
couple = NPC(
    "an attractive couple", ["blunt", "cigarette", "chewing gum"], 20, dance_floor
)
every_NPC = [partner, smile, misha, tanktop, pusher, hottest]
people_in_party = [partner, smile, misha]

##############################
print(smile.times_talked)
SmileTimes0 = Scene("SmileTimes0", smile, smiletimes0content)
SmileTimes0.run_scene()
print(smile.times_talked)
##Figure out time.thirty minute update thingy