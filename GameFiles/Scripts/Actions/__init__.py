from .MoveSc import Move, move
from .Use_ItemSc import Use_Item, use_item
from .Tap_WaterSc import Tap_Water, tap_water
from .CheckSc import Check, check
from .TalkSc import Talk, talk
from .DanceSc import Dance, dance
from .BorrowSc import Borrow, borrow

#########################################################################
#############################   INSTANCES   #############################
#########################################################################

dict_of_actions = {
    "Move": move,
    "Use": use_item,
    "Tap Water": tap_water,
    "Check": check,
    "Talk": talk,
    "Dance": dance,
    "Borrow": borrow,
}
