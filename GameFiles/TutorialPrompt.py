from GameFiles.Scenes.TutorialContent import tutorialscene


def tutorial_prompt(player, yesorno):
    print("Tutorial? (y/n) ", end="")
    op = yesorno()
    if op == True:
        tutorialscene.run_scene(player)
