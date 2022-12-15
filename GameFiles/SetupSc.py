def setup():
    """sets up the whole game and returns player object with everything assigned"""
    from GameFiles.Scenes.PartnerScenes.Compile import partnerscenes
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
    NPCs["partner"].location = rooms["smoking room"]
    NPCs["smile"].location = rooms["dance floor"]
    NPCs["russian"].location = rooms["dance floor"]

    print("SET UP.")
    print("")
    print(player.gameover)
    print(time)

    player.time.hour = 00
    player.time.minute = 00
    return player
