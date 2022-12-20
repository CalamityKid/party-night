from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks.SceneSc import Scene
from .CoupleGameover import couplegameovercontent
from .PartnerGameover import partnergameovercontent
from .PusherGameover import pushergameovercontent
from .RussianGameover import russiangameovercontent
from .SmileGameover import smilegameovercontent
from .TanktopGameover import tanktopgameovercontent
from ...Logo import logoscene


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
    sleep(4)

    logoscene.run_scene(player)

    for key, scene in gameover_scenes.items():
        scene.run_scene(player)
        sleep(2)

    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | words & code  |   by  | Joel Pantaleón Tejada | o   o |")
    sleep(2)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o |  Marc Perelló | o   o |  recorded & cleaned sound fx  |")
    sleep(2)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o |     TOOLS     | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o |  Yarn Spinner Editor  |  as  visual  writing aid  | o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o |  ASCII  Gen   |   at  |   network-science.de  | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | ASCII Patterns  from  | o   o |  asciiart.eu  | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    sleep(2)
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+    Dedicated to   +---+---+---+---+---|")
    print("|  o | o   o |    Every lousy party at Sala Tango    | o   o |")
    print("|+---+---+---+---+-  in which against all odds  -+---+---+---|")
    sleep(3)
    print("|  o | o   o | we still managed to have a great time | o   o |")
    sleep(3)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    sleep(2)
    print("º>==========================================================<º")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o  Special Thanks to:     | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    sleep(2)
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+---+---+ Cr & Am for critical early counsel    +---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    sleep(2)
    print("|+---+---+---+  Au, Ad, Ra, Kr for the encouragement +---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    sleep(2)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---   Marc  and  Edu            Oc, Hc, Ms     +---+---+---|")
    sleep(2)
    print("|  o |     for the support,          Rb, Eo & Gv     | o   o |")
    sleep(2)
    print("|+---+---+---+  love and            for inspiration  +---+---|")
    sleep(2)
    print("|  o | o   o | o   patience.            and laughs.  | o   o |")
    sleep(2)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("|+---+--            Thanks for playing !!      --+---+---+---|")
    print("|  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o |")
    print("º>==========================================================<º")
    sleep(5)
