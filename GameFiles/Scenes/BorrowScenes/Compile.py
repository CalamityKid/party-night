from ...Scripts.Blocks.SceneSc import Scene
from .RussianPoppers import russianpopperscontent
from .SmileG import smileGcontent
from .BorrowGum import borrowgumcontent
from .PartnerK import partnerkcontent


def assemble_borrow_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    russianpoppers = Scene("RussianPoppers", russianpopperscontent)
    smileG = Scene("SmileG", smileGcontent)
    borrowGum = Scene("BorrowGum", borrowgumcontent)
    partnerK = Scene("PartnerK", partnerkcontent)

    return {
        "your russian friend": russianpoppers,
        "the smile ambassador": smileG,
        "the attractive couple": borrowGum,
        "your partner": partnerK,
    }


borrow_scenes = assemble_borrow_scenes()
