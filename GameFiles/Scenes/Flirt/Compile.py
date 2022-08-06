from ...Scripts.Blocks.SceneSc import Scene
from .CoupleFlirt import coupleflirtcontent

# from .PartnerFlirt import partnerflirtcontent
from .PusherFlirt import pusherflirtcontent
from .RussianFlirt import russianflirtcontent
from .SmileFlirt import smileflirtcontent

# from .TanktopFlirt import tanktopflirtcontent


def assemble_flirt_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    coupleflirt = Scene("coupleflirt", coupleflirtcontent)
    # partner = Scene("partnerflirt", partnerflirtcontent)
    pusher = Scene("pusherflirt", pusherflirtcontent)
    russian = Scene("russianflirt", russianflirtcontent)
    smile = Scene("smileflirt", smileflirtcontent)
    # tanktop = Scene("tanktopflirt", tanktopflirtcontent)

    return {
        "the attractive couple": coupleflirt,
        # "your partner": partnerflirtcontent,
        "your new mercantile friend": pusher,
        "your russian friend": russian,
        "the smile ambassador": smile,
        # "the cutie in the tank top": tanktopflirtcontent,
    }


flirtscenes = assemble_flirt_scenes()
