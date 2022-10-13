from .SmileScenes.Compile import smilescenes
from .CoupleScenes.Compile import couplescenes
from .RussianScenes.Compile import russianscenes
from .TanktopScenes.Compile import tanktopscenes
from .PartnerScenes.Compile import partnerscenes
from .PusherScenes.Compile import pusherscenes
from ..Input import yesorno


def scene_select(player, actor):
    if actor.name == "your partner":
        print("You turn to your partner ", end="")
    else:
        print("You walk up to", str(actor.name) + " ", end="")

    if player.debug == True:
        print("Times talked is now", str(actor.times_talked) + ".")

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
    elif actor == player.NPCs["pusher"]:
        scene_dict_used = pusherscenes
    ######## scene exceptions
    if (
        (actor == player.NPCs["couple"])
        and (player.mouth < 20)
        and (couplescenes["CoupleGum"].has_run == False)
    ):
        return couplescenes["CoupleGum"].run_scene(player)

    elif "Gathering" in player.memories and player.time.hour < 5:
        if (
            hasattr(actor, "convinced") == True
            and actor.location.name != "the dance floor"
            and scene_dict_used["Convinced"].has_run != True
        ):
            return scene_dict_used["Convinced"].run_scene(player)

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
