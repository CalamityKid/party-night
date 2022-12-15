def gameloop():
    from GameFiles.Input import yesorno
    from .SetupSc import setup
    from .TutorialPrompt import tutorial_prompt
    from .Logo import logoscene
    from .RunGame import run_game
    from GameFiles.Scenes.Start import startscene

    player_object_game = setup()
    logoscene.run_scene(player_object_game)
    tutorial_prompt(player_object_game, yesorno)
    startscene.run_scene(player_object_game)
    run_game(player_object_game)
