from GameFiles.Scripts.Blocks.SceneSc import Scene
from time import sleep


def logocontent(player):
    print("º>==========================================================<º")
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o   o | o  __ | o   o | o   o | o   o |")
    sleep(1)
    print("|+---+---+---+  ____  ____ ______/ /___  __  +---+---+---+---|")
    print("|  o | o   o   / __ \/ __ `/ ___/ __/ / / /  | o   o | o   o |")
    print("|+---+---+--  / /_/ / /_/ / /  / /_/ /_/ /  -+---+---+---+---|")
    sleep(1)
    print("|  o | o     / .___/\__,_/_/   \__/\__, /  o | o   o | o   o |")
    print("|+---+---+  /_/    --+---+---+  _ /____/      __  ---+---+---|")
    print("|  o | o   o | o   o |   ____  (_)___ _/ /_  / /_    | o   o |")
    sleep(1)
    print("|+---+---+---+---+---+  / __ \/ / __ `/ __ \/ __/   -+---+---|")
    print("|  o | o   o | o   o   / / / / / /_/ / / / / /_      | o   o |")
    print("|+---+---+---+---+--  /_/ /_/_/\__, /_/ /_/\__/  +---+---+---|")
    sleep(1)
    print("|  o | o   o | o   o          /____/               o | o   o |")
    print("|+---+---+---+---+---+---+---+---+---+---+---+ v1.0 -+---+---|")
    print("|  o | o   o | o   o | o   o | o   o |  A Flame Tree Game  o |")
    sleep(1)
    print("|+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")
    print("|  o | o   o | o   o | o | o   o | o   o | o | o   o | o   o |")
    print("º>==========================================================<º")
    sleep(1)


logoscene = Scene("Logo Scene", logocontent)
