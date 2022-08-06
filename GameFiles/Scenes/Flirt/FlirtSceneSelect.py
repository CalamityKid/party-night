from ..Format.Bark import flirt_bark_good, flirt_bark_bad
from ..Format.FlirtCalculations import flirt_calculations

outcome = None
        outcome = flirt_calculations(player_object)
        if outcome == True:
            print(flirt_bark_good(player_object))
        elif outcome == False:
            print(flirt_bark_bad(player_object))
        return None