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

print(dance_floor)
