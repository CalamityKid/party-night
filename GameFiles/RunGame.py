def run_game(player):

    from time import sleep
    from GameFiles.ScheduleSc import update_schedule
    from GameFiles.Scripts.Format.Narration import narrate_actions
    from GameFiles.Input import player_choose_action
    from .Scenes.Gameover.Compile import assemble_and_run_gameover_scenes

    non_counter = 0
    update_schedule()

    while player.gameover == False:
        action_met = None
        narrate_actions(player)
        sleep(1)
        player.narrate_stats(True)
        action_met = player_choose_action(player)
        sleep(2)
        if action_met == True or non_counter == 3:
            player.time.ten_minutes()
            non_counter = 0
        elif action_met != True:
            non_counter += 1

        if player.gameover == False:
            update_schedule()
            sleep(3)

    assemble_and_run_gameover_scenes(player)
    sleep(2)
