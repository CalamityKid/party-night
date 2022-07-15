from ...Scripts.Blocks.SceneSc import Scene
from .CoupleDance import coupledancecontent
from .RussianDance import russiandancecontent
from .SmileDance import smiledancecontent
from .TanktopDance import tanktopdancecontent


def assemble_dance_scenes():
    coupledance = Scene("couple", coupledancecontent)
    russiandance = Scene("russian", russiandancecontent)
    smiledance = Scene("smile", smiledancecontent)
    tanktopdance = Scene("tanktop", tanktopdancecontent)

    return {
        "the attractive couple": coupledance,
        "your russian friend": russiandance,
        "the smile ambassador": smiledance,
        "the cutie in the tank top": tanktopdance,
    }


dance_scenes = assemble_dance_scenes()