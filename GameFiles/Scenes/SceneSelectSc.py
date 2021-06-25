from .SmileScenes.Compile import smilescenes
from .CoupleScenes.Compile import couplescenes
from .RussianScenes.Compile import russianscenes
from .TanktopScenes.Compile import tanktopscenes
from .PartnerScenes.Compile import partnerscenes
from ..Input import yesorno


def scene_select(player, actor):
    print(
        "You walk up to",
        str(actor.name)
        + ". "
        + "Times talked is now: "
        + str(actor.times_talked)
        + ".",
    )
    print("")
    scene_dict_used = {}
    scene_name = "Times"

    ####select the scene
    scene_name = scene_name + str(actor.times_talked)
    ####select the scene dictionary

    if actor == player.NPCs["smile"]:
        scene_dict_used = smilescenes
    elif actor == player.NPCs["couple"]:
        scene_dict_used = couplescenes
    elif actor == player.NPCs["russian"]:
        scene_dict_used = russianscenes
    elif actor == player.NPCs["tanktop"]:
        scene_dict_used = tanktopscenes
    elif actor == player.NPCs["partner"]:
        scene_dict_used = partnerscenes

    ######## scene exceptions
    if actor == player.NPCs["smile"] and actor.times_talked >= 2:
        print("Do you wanna ask for G? ", end="")
        option = yesorno()
        if option == True:
            return smilescenes["SmileG"].run_scene(player)

    elif (
        (actor == player.NPCs["couple"])
        and (player.mouth < 20)
        and (couplescenes["CoupleGum"].has_run == False)
    ):
        return couplescenes["CoupleGum"].run_scene(player)

    elif actor == player.NPCs["russian"]:
        print("Do you wanna ask for poppers? ", end="")
        option = yesorno()
        if option == True:
            return russianscenes["RussianPoppers"].run_scene(player)

    ######################### end exceptions, if no exceptions, run the scene
    try:
        return scene_dict_used[scene_name].run_scene(player)
    except KeyError:
        print(
            "Couldn't find this scene. Key Error:",
            str(scene_dict_used),
            str(scene_name),
        )
        return None
