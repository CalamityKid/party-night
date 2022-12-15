def gameloop():
    from GameFiles.Input import yesorno
    from .SetupSc import setup
    from .TutorialPrompt import tutorial_prompt
    from .RunGame import run_game
    from GameFiles.Scenes.Start import startscene

    player = setup()
    tutorial_prompt(player, yesorno)
    # startscene.run_scene(player)
    run_game(player)

    del player
