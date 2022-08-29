from .Bark import flirt_bark_bad, flirt_bark_good

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


def flirting(player_object):
    """takes player object, runs flirt_calculations which returns a boolean, prints the corresponding text (good or bad_flirt_bark) and returns the boolean
    the flirt calculations formula is the formula is [ (mouth + (lit/2) + (high/3)) - coolness ] the number to beat for True is 70"""
    outcome = None
    outcome = flirt_calculations(player_object)
    if outcome == True:
        print(flirt_bark_good(player_object))
    elif outcome == False:
        print(flirt_bark_bad(player_object))
    return outcome
