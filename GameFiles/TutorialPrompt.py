from GameFiles.Scenes.TutorialContent import tutorialscene
from time import sleep


def tutorial_prompt(player, yesorno):
    print("")
    print("      Would you play the tutorial first? (y/n) ", end="")
    op = yesorno()
    if op == True:
        tutorialscene.run_scene(player)
    else:
        sleep(1)
        print("")
        print("   If you change your mind, just type TUTORIAL at any time.")
        sleep(2)
        print("")
