from .SmileScenes.Compile import smilescenes
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
    if actor == player.NPCs["smile"]:
        if actor.times_talked == 0:
            return smilescenes["Times0"].run_scene(player)
        if actor.times_talked == 1:
            return smilescenes["Times1"].run_scene(player)
        if actor.times_talked >= 2:
            print("Do wanna ask for G? ", end="")
            option = yesorno()
            if option == True:
                return smilescenes["BorrowG"].run_scene(player)
            elif option == False:
                if actor.times_talked == 2:
                    return smilescenes["Times2"].run_scene(player)
                elif actor.times_talked == 3:
                    return smilescenes["Times3"].run_scene(player)
                elif actor.times_talked == 4:
                    return smilescenes["Times4"].run_scene(player)
