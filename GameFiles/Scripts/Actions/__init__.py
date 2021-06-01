from .MoveSc import Move, move
from .Use_ItemSc import Use_Item, use_item
from .Tap_WaterSc import Tap_Water, tap_water

__all__ = ["MoveSc", "Use_ItemSc"]

#########################################################################
#############################   INSTANCES   #############################
#########################################################################

dict_of_actions = {"Move": move, "Use": use_item, "Tap Water": tap_water}
