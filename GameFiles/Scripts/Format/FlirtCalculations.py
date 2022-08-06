# flirt formula is: [[ (mouth + (lit/2) + (high/3)) - coolness ]]
# it's succesful if it's more than 70


def flirt_calculations(player_obj):
    """Takes player object, returns boolean depending on the stats
    the formula is [ (mouth + (lit/2) + (high/3)) - coolness ]"""
    answer = None
    answer = (
        player_obj.mouth + (player_obj.lit / 2) + (player_obj.high / 3)
    ) - player_obj.coolness
    answer = int(answer)
    if answer >= 70:
        answer = True
    elif answer < 70:
        answer = False
    return answer
