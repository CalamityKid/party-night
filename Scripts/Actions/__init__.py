from .MoveSc import Move, move
from .Use_ItemSc import Use_Item, use_item

__all__ = ["MoveSc", "Use_ItemSc"]

#########################################################################
#############################   INSTANCES   #############################
#########################################################################

dict_of_actions = {"Move": move, "Use": use_item}
