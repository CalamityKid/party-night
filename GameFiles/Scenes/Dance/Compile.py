from ...Scripts.Blocks.SceneSc import Scene
from .CoupleDance import coupledancecontent
from .RussianDance import russiandancecontent
from .SmileDance import smiledancecontent
from .TanktopDance import tanktopdancecontent
from .ChangedMusic import changedmusiccontent
from .PartnerDance import partnerdancecontent


def assemble_dance_scenes():
    coupledance = Scene("couple", coupledancecontent)
    russiandance = Scene("russian", russiandancecontent)
    smiledance = Scene("smile", smiledancecontent)
    tanktopdance = Scene("tanktop", tanktopdancecontent)
    partnerdance = Scene("partner", partnerdancecontent)
    changedmusic = Scene("Changed Music Scene", changedmusiccontent)

    return {
        "the attractive couple": coupledance,
        "your russian friend": russiandance,
        "the smile ambassador": smiledance,
        "the cutie in the tank top": tanktopdance,
        "your partner": partnerdance,
        "Changed Music": changedmusic,
    }


dance_scenes = assemble_dance_scenes()
