import time
from ...Input import yesorno
from ...Scripts.Blocks.SceneSc import Scene
from .CoupleGameover import couplegameovercontent
from .PartnerGameover import partnergameovercontent
from .PusherGameover import pushergameovercontent
from .RussianGameover import russiangameovercontent
from .SmileGameover import smilegameovercontent
from .TanktopGameover import tanktopgameovercontent


def assemble_and_run_gameover_scenes(player):
    partnerGO = Scene("partner", partnergameovercontent)
    coupleGO = Scene("couple", couplegameovercontent)
    smileGO = Scene("smile", smilegameovercontent)
    pusherGO = Scene("pusher", pushergameovercontent)
    russianGO = Scene("russian", russiangameovercontent)
    tanktopGO = Scene("tanktop", tanktopgameovercontent)

    gameover_scenes = {
        "partner": partnerGO,
        "couple": coupleGO,
        "smile": smileGO,
        "pusher": pusherGO,
        "russian": russianGO,
        "tanktop": tanktopGO,
    }

    print("     And that's the end of the night! Ready for the ending? ", end="")
    option = yesorno()
    if option == True:
        print("       Alright, here we go! Lay back and enjoy!")
    elif option == False:
        print("Ready or not, here we go! Lay back and enjoy!")
    time.sleep(4)

    print("º>==========================================================<º")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o  __ | o   o | o   o | o   o |")
    print("|+---+---+---+  ____  ____ ______/ /___  __  +---+---+---+---|")
    print("|  o | o   o   / __ \/ __ `/ ___/ __/ / / /  | o   o | o   o |")
    print("|+---+---+--  / /_/ / /_/ / /  / /_/ /_/ /  -+---+---+---+---|")
    print("|  o | o     / .___/\__,_/_/   \__/\__, /  o | o   o | o   o |")
    print("|+---+---+  /_/    --+---+---+  _ /____/      __  ---+---+---|")
    print("|  o | o   o | o   o |   ____  (_)___ _/ /_  / /_    | o   o |")
    print("|+---+---+---+---+---+  / __ \/ / __ `/ __ \/ __/   -+---+---|")
    print("|  o | o   o | o   o   / / / / / /_/ / / / / /_      | o   o |")
    print("|+---+---+---+---+--  /_/ /_/_/\__, /_/ /_/\__/  +---+---+---|")
    print("|  o | o   o | o   o          /____/               o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o |  by Joel Pantaleón Tejada   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("º>==========================================================<º")

    for key, scene in gameover_scenes.items():
        scene.run_scene(player)
        time.sleep(3)

    print("º>==========================================================<º")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o  Special Thanks to:     | o   o | o   o | o   o | o   o |")
    print("|+---    Marc and Edu             My friends   --+---+---+---|")
    print("|  o |     for the support,         for the inspiration    o |")
    print("|+---+---+     love and patience.          and the laughs. --|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+--            Thanks for playing !!      --+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("º>==========================================================<º")

    time.sleep(6)
